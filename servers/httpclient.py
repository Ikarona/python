#!/usr/bin/python3
import socket
import os
import time
import pickle
import requests 
import csv
from pprint import pprint

path = "/home/ikarona/Desktop/pyfon/4task/dataSet12.csv"

NUM = int(input())
while NUM < 40:
    print("NUM ONLY > 40")
    NUM = int(input())
CMD = ""
CMD = input()


with open(path, 'r', errors='ignore',encoding = "ISO8859-1") as f:
    read = csv.reader(f, delimiter = ';')
    to_send = pickle.dumps(list(read)[1:NUM+1])#скидываем только нужную часть списка
r = requests.post('http://127.0.0.1:8000/'+CMD, data=to_send)

back_res = r.content
fin_res = pickle.loads(back_res)
pprint(fin_res)
