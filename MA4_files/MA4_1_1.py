
"""
Solutions to module 4
Review date:
"""

student = "Agnes Leth"
reviewer = ""


import random as r
import matplotlib.pyplot as plt
import math as m 

def approximate_pi(n):
    # Write your code here
    n_c = 0 #points inside the circle
    n_s = 0 #pints outside the circle
    
    x_inside = []
    y_inside = []

    x_outside = []
    y_outside = []

    for _ in range(n):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        dis = (x**2+y**2)**(1/2)
        if dis <= 1:
             n_c += 1
             x_inside.append(x)
             y_inside.append(y)
        else: 
             n_s += 1
             x_outside.append(x)
             y_outside.append(y)
    
    pi_approx = 4*n_c/n
    pi_exact = m.pi
    
    fig, ax = plt.subplots()

    ax.scatter(x_inside, y_inside, color='red', s=1)
    ax.scatter(x_outside, y_outside, color='blue', s=1)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_title(f'Approximate PI using Monte Carlo, n = {n}')
    plt.savefig(f'{n}.png')
	plt.show()

    print(f'n = {n}')
    print(f'n_c = {n_c}, n_s = {n_s}')
    print(f'PI approximate = {pi_approx}')
    print(f'PI exact = {pi_exact} \n')

    return pi_approx
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
