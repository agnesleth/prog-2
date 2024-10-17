
"""
Solutions to module 4
Review date:
"""

student = "Agnes Leth"
reviewer = ""

import math as m
import random as r
from time import perf_counter as pc
import concurrent.futures as future
import numpy
from functools import reduce
import multiprocessing as mp

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    points = [[r.uniform(-1,1) for _ in range(d)] for _ in range(n)] 
    distance = lambda point: numpy.sqrt(reduce(lambda acc, x: acc + x**2, point, 0)) 
    distances = list(map(distance, points))
    n_c = len(list(filter(lambda p: p <= 1, distances)))
    V = 2**d*n_c/n
    return  V

def hypersphere_exact(n,d):
    return m.pi**(d/2)/m.gamma(d/2 + 1) 

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function  
     with future.ProcessPoolExecutor() as executor:
        results = [executor.submit(sphere_volume, n, d) for _ in range(np)]
        volumes = [r.result() for r in future.as_completed(results)]
    
        return numpy.mean(volumes)
      

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
     points_per_process = n//np
    
    # Parallel computation by splitting the data
     with future.ProcessPoolExecutor() as executor:
        #submit each process with its own chunk of points
        results = [executor.submit(sphere_volume, points_per_process, d) for _ in range(np)]

        total_volume = 0
        for r in future.as_completed(results):
            total_volume += r.result()
        
    # The final volume estimate is the average of all results
        return total_volume/np
 

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10

#time both the sequential and parallel versions to compare their performance.
    start = pc()
    for y in range(np):
        sphere_volume(n,d)
    end = pc()
    print(f"Sequential execution took: {end - start} seconds")

    # Parallel run using ProcessPoolExecutor
    start = pc()
    sphere_volume_parallel1(n, d, np)
    end = pc()
    print(f"Parallel execution took: {end - start} seconds")

# part 2 
    n = 1000000
    d = 11
    np = 10

    start = pc()
    for _ in range(np):
        sphere_volume(n // np, d)
    end = pc()
    print(f"Sequential execution took: {end - start} seconds")

    start = pc()
    volumes = sphere_volume_parallel2(n, d, np)
    end = pc()
    print(f"Parallel execution took: {end - start} seconds")

    print(hypersphere_exact(n, d))
    print(sphere_volume_parallel1(n,d,np))
    print(sphere_volume_parallel2(n,d,np))

if __name__ == '__main__':
	main()



"""
Part 1: 
ProcessPoolExecutor: This creates a pool of processes. Each process will run an instance of sphere_volume independently.

"""