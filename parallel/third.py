#! /usr/bin/python3 -W ignore
'''
Librosa parallel algo. Processes are faster then linear.
'''
import os
from multiprocessing import Process
import time
import librosa
import numpy as np

LIST_OF_FILES = []

def filllles_in_list(files_dir):
    for root, directories, files in os.walk(files_dir):
        for file in files:
            LIST_OF_FILES.append(root + '/' + file)

def for_parellel(where_to_write_dir, files_dir, start, stop):
    for list_iter in range(start, stop):
        w_2 = where_to_write_dir + '/'+ LIST_OF_FILES[list_iter][len(
            files_dir):LIST_OF_FILES[list_iter].rfind('/')]
        if not os.path.exists(w_2):
            os.makedirs(w_2)
        for_librosa = LIST_OF_FILES[list_iter]
        file_name = LIST_OF_FILES[list_iter][LIST_OF_FILES[list_iter].rfind('/')+1:]
        y_1, sr_1 = librosa.core.load(for_librosa)
        a_array = librosa.feature.mfcc(y=y_1, sr=sr_1)
        buf = w_2 +'/' + file_name[:len(file_name) - 4]
        np.save(buf, a_array)

if __name__ == '__main__':

    DATASET_DIR = ''
    OUT_DIR = ''
    DATASET_DIR = input()
    OUT_DIR = input()
    OUT_DIR += '/'  #case u forgot / in link

    filllles_in_list(DATASET_DIR)

    LENGTH = len(LIST_OF_FILES)

    PROCESS1 = Process(target=for_parellel, args=(OUT_DIR, DATASET_DIR,
        0, LENGTH // 4))
    PROCESS2 = Process(target=for_parellel, args=(OUT_DIR, DATASET_DIR,
        LENGTH // 4 + 1, LENGTH // 2))
    PROCESS3 = Process(target=for_parellel, args=(OUT_DIR, DATASET_DIR,
        LENGTH // 2 + 1, 3*LENGTH // 4))
    PROCESS4 = Process(target=for_parellel, args=(OUT_DIR, DATASET_DIR,
        3 * LENGTH // 4 +1, LENGTH))

    START_TIME = time.time()
    PROCESS1.start()
    PROCESS2.start()
    PROCESS3.start()
    PROCESS4.start()

    PROCESS1.join()
    PROCESS2.join()
    PROCESS3.join()
    PROCESS4.join()

    T_RES =  time.time() - START_TIME
    print('Runtime: ', T_RES)
    print('Speed', LENGTH / T_RES)
