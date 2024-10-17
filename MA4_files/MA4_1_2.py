
"""
Solutions to module 4
Review date:
"""

student = "Agnes Leth"
reviewer = ""

import math as m
import random as r
import numpy as np
from functools import reduce

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    
    #generate n points, where each point has d coordinates
    points = [[r.uniform(-1,1) for _ in range(d)] for _ in range(n)] #list comprehension

    #Euclidean distance
    distance = lambda point: np.sqrt(reduce(lambda acc, x: acc + x**2, point, 0)) #lamda function and reduce()

    # Use map() to calculate distances for all points
    distances = list(map(distance, points))
    
    #use filter to count the points inside the sphere
    n_c = len(list(filter(lambda p: p <= 1, distances))) #filter
        
    V = 2**d*n_c/n

    return V
 

def hypersphere_exact(n,d):
   return m.pi**(d/2)/m.gamma(d/2 + 1) #lamda fuction
     
def main():
    n = 100000
    d = 11
    print(sphere_volume(n,d))
    print(hypersphere_exact(n,d))


if __name__ == '__main__':
	main()
     

"""
1. List comprehension: returns a list of coordinates; points = [[r.uniform(-1,1) for _ in range(d)] for _ in range(n)] 
2. lamda function: simple functions, also called anonymous functions
3. reduce(): Purpose of reduce is to reducean iterable (list, tuple, etc) down to a value
    (lambda acc, x: acc + x**2, point, 0) takes the list, point, and for each coord x squares it to the sum acc, acc starts at 0
    reduce() to reduce to a value, returns a a sum of squares
    take sqrt for the Euclidean distance
4. map() applies distance() to each point, transforming the list of points into a list of distances.
5.filter(): Takes 2 arg: 
    1) A function that returns True or False for each element.
    2) An iterable (in this case, points, which is a list of random points).
    (lambda p: p <= 1, distances): It filters the distances list to keep only those distances that are less than or equal to 1
    The filter() function only returns thoose points where lamda is True
    Lastly, needs to be converted to a list to take the lenght
"""
