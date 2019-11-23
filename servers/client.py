#!/usr/bin/python3
import socket
import os
import time
import pickle

path = "/home/ikarona/Рабочий стол/pyfon/4task/dataSet12.csv"
print("If u wanna test it u should better delete time.sleep()")
NUM = int(input())

CMD = input()

def FILE_SENDER(socket):
    sum1 = 0
    with open(path,'r', errors = 'ignore') as f:
        for line in f:
            sum1 += len(line)
            socket.send(str(len(line)).encode("utf8"))
            time.sleep(0.01)
            socket.send(b'^')
            time.sleep(0.1)
            socket.send(line.encode("utf8"))
    print("Finished: ", os.getpid())

data = {"command" : CMD,"size" : NUM}

with socket.create_connection(("127.0.0.1", 3031)) as sock:
    sock.send(str(data).encode("utf8"))
    time.sleep(0.1)
    while True:
        check = sock.recv(1024)
        time.sleep(0.1)
        if not check:
            break

        if check.decode("utf8") == "GOT":
            FILE_SENDER(sock)
        break
    answer = sock.recv(2048)
    time.sleep(1)
    answ = pickle.loads(answer)
    print(answ,flush=True)
