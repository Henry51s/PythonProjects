import numpy as np
import matplotlib.pyplot as plt

p = 1.225;
c = 0.47;
a = np.pi*25;
m = 10;

alpha = (0.5*p*c*a)/m

vSol = []

def domain(domain):
    d = []
    for i in range(domain):
        d.insert(i,i)
    return d

def dvdt(constants, v):
    return (constants * v * v * -1)

def euler_method(constants,v0,h,n):
    for i in range(n):
        v = v0 + h*dvdt(constants,v0)
        v0 = v
        vSol.insert(i,v)
    plt.plot(domain(n),vSol)
    plt.show()
euler_method(alpha,10,0.01,100)