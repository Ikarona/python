#!/usr/bin/python3
import socket
import string 
import ast
from pycorenlp import StanfordCoreNLP
from pprint import pprint
import time 
import pickle
from http.server import HTTPServer, BaseHTTPRequestHandler

import multiprocessing
import os
import pickle

def STAT(lst):
    words = {}
    for i in lst:
        try :
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
    return pickle.dumps(for_send)

def ENTI(lst):
    nlp = StanfordCoreNLP('http://localhost:9000')
    for i in lst:
        print(i)
        try:
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
        except:
            pass
    res = " ".join(pos)
    #print(res)
    return pickle.dumps(pos)

class RequestHeandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        res =b''
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data_arr = pickle.loads(data)
        self._set_headers()
        if self.path == '/STAT':
            res = STAT(data_arr)
        elif self.path == '/ENTI':
            res = ENTI(data_arr)
        else:
            print("ERROR")
        self.wfile.write(res)

def run(server_class=HTTPServer, handler_class=RequestHeandler, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()