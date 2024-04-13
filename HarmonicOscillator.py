from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#Equation used: y''+y'+3y=0

m=10 #Mass
k=1000 #Spring Constant
b=100 #Friction Constant

y0=10 #Inital Position
y_dot0=10000 #Initial Velocity

runtime = 20
nPoints = 10000

def solver(y,t):
    return [y[1], -(b/m)*y[1]-(k/m)*y[0]]

def main():
    time = np.linspace(0,runtime,nPoints)
    sol = odeint(solver,[y0,y_dot0],time)
    return sol[:, 0]


plt.figure()
plt.axhline(0, color = "blue", linestyle = "--")
plt.plot(main())
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()