#!/usr/bin/python3
import socket
import ast
import pickle
import time 
import multiprocessing
import os
from pycorenlp import StanfordCoreNLP
from pprint import pprint

def Checker(data_fs, connection):
    RECIEVED_DATA = ast.literal_eval(data_fs)
    lst = DATA_READER(connection, RECIEVED_DATA["size"])
    lst1 = lst
    lst2 = lst
    if RECIEVED_DATA['command'] == "STAT":
        return STAT(lst1)
    if RECIEVED_DATA['command'] == "ENTI":
        return ENTI(lst2)

def STAT(lst): #тк dataset попорчен -> необходимо много try-except
    words = {}
    for i in lst:
        try:
            line = i[6]
            for word in line.split(" "):
                if word != '':
                    try:
                        words[word] += 1
                    except KeyError:
                        words[word] = 1
        except:
            pass
    pairs = sorted(words.items(), key=lambda x: x[1], reverse=True)
    rts = {}
    for i in lst:
        try:
            author = i[3]
            retv = i[8]
            rts[author] = retv
        except:
            pass
    re_au = sorted(rts.items(), key=lambda x:x[1], reverse=True)
    countries_t = {}
    for c in lst:
        try:
            country = c[11]
            if country != '' and country.isalpha() and country.isupper():
                try:
                    countries_t[country] += 1
                except KeyError:
                    countries_t[country] = 1
        except:
            pass
    cnt_t = sorted(countries_t.items(), key=lambda x: x[1], reverse=True)
    countries_rts = {}
    for i in lst:
        try:
            line = i[6]
            if line.find('RT') != -1:
                country = i[11]
                if country != '' and country.isalpha():
                    try:
                        countries_rts[country] += 1
                    except KeyError:
                        countries_rts[country] = 1
        except:
            pass
    cnt_rts = sorted(countries_rts.items(), key=lambda x: x[1], reverse=True)
    for_send = {"10pop_words" : pairs[:10],
                "10pop_auth" : re_au[:10],
                "tweet_cnts" : cnt_t,
                "retweet_cnts" : cnt_rts}
    return for_send

def ENTI(lst):
    nlp = StanfordCoreNLP('http://localhost:9000')
    for i in lst:
        print(i)
        text = i[6]
        result = nlp.annotate(text,
                       properties={
                           'annotators': 'ner',
                           'outputFormat': 'json',
                           'timeout': 10000,
                       })
        pos = []
        for word in result["sentences"][0]['tokens']:
            pos.append('{} ({})'.format(word['word'], word['ner']))
    res = " ".join(pos)
    #print(res)
    return pos

def DATA_READER(connection, size):# принимаем по одному символу
    lst = []
    full_strlen = 0
    string = ''
    FLAG = False
    strnum = 0
    while not FLAG and strnum < size:#считываем построчно
        symb = ''
        strlen = 0
        while True:#клиент передает длину считываемой строки по одному символу, считываем
            symb = connection.recv(1)
            time.sleep(0.1)
            if symb == b'^':
                break
            if symb == b'':
                FLAG = True
                break
            if symb.decode("utf8").isdigit():
                #print("symb = ", symb.decode("utf8"),flush=True)
                strlen = strlen * int(10.0) + int(symb.decode("utf8"))
        full_strlen += strlen
        if not FLAG:
            #print("strlen = ", strlen,flush=True)
            info = connection.recv(strlen).decode("utf8")
            time.sleep(0.1)

            newstr = ''#dataset попорчен -> считываем пока не будет хватать столбцов
            while info.count(';') < 18: 
                strlen = 0
                while True:
                    symb = connection.recv(1)
                    time.sleep(0.1)
                    if symb == b'^':
                        break
                    if symb == b'':
                        FLAG = True
                        break
                    if symb.decode("utf8").isdigit():
                        #print("symb = ", symb.decode("utf8"))
                        strlen = strlen * int(10.0) + int(symb.decode("utf8"))
                if not FLAG:
                    full_strlen += strlen
                    #print("strlen = ", strlen,flush=True)
                    newstr = connection.recv(strlen).decode("utf8")
                    time.sleep(0.1)
                    newstr = newstr.replace('"',"")
                    newstr = newstr.replace("\n"," ")
                    info += ' ' + newstr
            info = info.replace("?","")#удаляем лишние символы из строк
            info = info.replace('"',"")
            info = info.replace("\n"," ")
            #print(newstr)

            lst.append(info)#добавляем в список
            strnum += 1
            string += info
    #print("FULL = ", full_strlen,flush=True)
    #print("strnum = ", strnum,flush=True)
    pprint(lst)
    i = 0
    #разделяем каждую строку по ; чтоб обрабатывать потом
    for x in lst:
        lst[i] = x.split(';')
        i+=1
    return lst

ANSWER_STR = b"GOT"

def worker(sock):
    conn, addr = sock.accept()
    print("pid", os.getpid(),flush=True)
    th = multiprocessing.Process(target=helper , args=(conn, addr))
    th.start()

def helper(conn, addr):
    print("connected client:", addr, flush=True)
    with conn:
        while True:
            data = conn.recv(1024)
            time.sleep(0.1)
            if not data:
                break
            print('data = ',data, flush=True)
            conn.sendall(ANSWER_STR)
            time.sleep(0.1)
            r_1 = Checker(data.decode("utf8"), conn)
            #print(pickle.dumps(r_1), flush=True)
            conn.sendall(pickle.dumps(r_1))
            time.sleep(0.1)
            conn.close()
            #pprint(r_1)


with socket.socket() as sock:
    sock.bind(("", 3031))# max port 65535
    sock.listen()
    workers_count = 3
    workers_list = [multiprocessing.Process(target=worker, args=(sock,))
                    for _ in range(workers_count)]

    for w in workers_list:
        w.start()

    for w in workers_list:
        w.join()