"""
Solutions to module VA 4

Student:
Mail:
"""
#!/usr/bin/env python3

#from person import Person
"""
Write a script that gives a plot for comparison of two approaches for Fibonacci numbers
"""
from numba import njit
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np

@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return (fib_numba(n-1) + fib_numba(n-2))

def fib_py(n):
    if n <= 1:
        return n
    else:
        return (fib_py(n-1) + fib_py(n-2))
    

n = np.linspace(20, 30)
numba_time = []
py_time = []

for i in n:
     start1 = perf_counter()
     fib_numba(i)
     stop1 = perf_counter()
     numba_time.append(stop1-start1)
     
for i in n:
     start2 = perf_counter()
     fib_py(i)
     stop2 = perf_counter()
     py_time.append(stop2-start2)

plt.plot(n, numba_time, label='fib_numba')
plt.plot(n, py_time, label='fib_py')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()

plt.plot(n, numba_time, label='fib_numba')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()




t1 = perf_counter() 
print(f'fib_numba: {fib_numba(47)}') 
t2 = perf_counter()
print(f'time calulateing fib_numba(47):', t2-t1)

t3 = perf_counter()
print(f'fib_py: {fib_py(47)}')
t4 = perf_counter()
print(f'time calulateing fib_py(47):', t4-t3)
    
def main():
	"""
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())
    """

if __name__ == '__main__':
	main()


"""What is the result for Fibonacci with n=47? Why?"""