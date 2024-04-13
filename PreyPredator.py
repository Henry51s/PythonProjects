import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#Given constants
a=.001 #Reproduction rate of rabbits
b=.01 #Interaction rate
c=.01 #Death rate of foxes
e=.001 #Reproduction rate of foxes

#Array of y-coordinates
rSol= []
fSol = []

def drdt(r,f):
    return (a*r)-(b*r*f)

def dfdt(r,f):
    return (e*b*r*f)-(c*f)

def domain(domain): #Returns array of x-coordinates
    d = []
    for i in range(domain):
        d.insert(i,i)
    return d

def euler_method(r0,f0,h,n):
    for i in range(n): #iterate it n months

        r = r0 + h*drdt(r0,f0)
        f = f0 + h*dfdt(r0,f0)
        r0 = r
        f0 = f

        rSol.insert(i,r)
        fSol.insert(i,f)

    plt.plot(domain(n),rSol)
    plt.plot(domain(n),fSol)
    plt.show()

euler_method(30,30,5,150)