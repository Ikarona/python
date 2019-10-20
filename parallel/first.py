#! /usr/bin/python3
'''
Librosa linear algo. Works slow.
'''
import os
import time
import librosa
import numpy as np

def filllles(where_to_write_dir, files_dir):
    for root, directories, files in os.walk(files_dir):
        for file in files:
            w_2 = where_to_write_dir + '/'+ root[len(files_dir):]
            if not os.path.exists(w_2):
                os.makedirs(w_2)
            y_1, sr_1 = librosa.core.load(root + '/' + file)
            a_array = librosa.feature.mfcc(y=y_1, sr=sr_1)
            buf = w_2 +'/' +file[:len(file) - 4]
            np.save(buf, a_array)

if __name__ == '__main__':
    OUT_DIR = ''
    DATASET_DIR = ''

    OUT_DIR = input()
    DATASET_DIR = input()

    START_TIME = time.time()

    filllles(OUT_DIR, DATASET_DIR)

    END_TIME = time.time()
    print("Time in sec:", END_TIME - START_TIME)
    SPEED = 36244 / (END_TIME - START_TIME)
    print("Speed:", SPEED)
