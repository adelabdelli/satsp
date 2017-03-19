from random import random
import math
import random
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np

valid=True
not_valid=False
nbr_city=5
distance=[[0,6,6,1,4],[6,0,8,3,5],[6,8,0,6,4],[1,3,6,0,2],[4,5,4,2,0]]
s0=[1,2,3,4,5]

# genrate a new solution by swaping the initials solutions
def swap(solution):
    i,j=0,0
    while j==i :
        i=random.randint(1,nbr_city-1)
        j=random.randint(1,nbr_city-1)
    temp=solution[i]
    solution[i]=solution[j]
    solution[j]=temp
    return solution

# test if there is not a duplicate cities
def testSol1(solution):
    for i in range(len(solution)):
        for j in range(i+1,len(solution)):
            if(solution[i]==solution[j]):
                return not_valid
    return valid

# test if the distance between the cities are not equal to zero
def testSol2(solution):
    for i in range(len(solution)-1):
        if distance[solution[i]-1][solution[i+1]-1]==0:
            return not_valid
    return valid

# generate new soltuion by swap and test it
def genrate(solution):
    s=swap(solution)
    while testSol1(s)==not_valid or testSol2(s)==not_valid :
        s=swap(solution)
    return s

# function of evaluating the solution by calculating the sum of distance
def cost(solution):
    c=0
    for i in range(len(solution)-1):
        c=c+distance[solution[i]-1][solution[i+1]-1]
    return c

def acceptance_probability(old_cost, new_cost, T):
    a=(float)((float)(new_cost-old_cost)/(float)(T))
    return np.exp(-a)

def anneal(solution,n=100,T=80.,alpha=0.8):
    old_cost = cost(solution)
    j=1
    while T >= 0.0000001:
        for i in range(n):
            new_solution = genrate(solution)
            new_cost = cost(new_solution)
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.uniform(0, 1):
                solution = new_solution
                old_cost = new_cost
                j+=1
                print("j= ",j)
            print("new solution = ",new_solution)
        T = T * alpha
    print("T final = ",T)
    return solution, old_cost


a, b = anneal(s0)
print("solution =", a, "\nold cost =", b,"\nnew solution cost =",cost(a))



