import time
import random
import multiprocessing as mp
from tqdm import tqdm
import numpy as np
import h5py
import pandas as pd

from multiprocessing import Process, Manager
np.random.seed(0)

rand_array = np.random.randint(10, size=(5000, 10000))
rand_list = [item for item in range(5000)]
rand_array = rand_array/1000
ar = []


def counter_addtion(counter, labels):  
    for item in labels:
        counter["{}".format(item)] = 0
    return counter

def diversity_addtion(counter, label, labels, ar, embedding):
    for other_label, other_embedding in ar:
        if label != other_label:
            distance = np.linalg.norm(embedding - other_embedding)  # euclidean distance
            counter["{}".format(label)] += distance
            
            #counter.update_counter(label, distance)
def diversity_addtion2(label, labels, ar, embedding):
    for other_label, other_embedding in ar:
        if label != other_label:
            distance = np.linalg.norm(embedding - other_embedding)  # euclidean distance
            counter["{}".format(label)] += distance     
def init_processes(d):
    global counter

    counter = d  

for row in range(0, len(rand_list)):
    ar.append([rand_list[row], rand_array[row,:]])
diversity_scores = []
start = time.time()
manager = Manager()
#counter = labels_counter(rand_list)
num_workers = 6
if __name__ == '__main__':
    
    counter = manager.dict()
    
    #jobs = []
    for item in rand_list:
        counter["{}".format(item)] = 0

    
    with mp.Pool(num_workers, initializer=init_processes, initargs=(counter,)) as p:
        results = p.starmap(diversity_addtion2, [(label, rand_list, ar, embedding) for label, embedding in ar])
    print(counter)

        
            
        
        

end = time.time()
print("time taken:{}".format(end-start))
