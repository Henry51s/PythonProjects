import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

#Constants and inital variables
g = 6.6743e-11
mass_1 = 2e30

initial_x = 0
initial_y = 10000

initial_vx = 10000000
initial_vy = 0

runtime = 10
time_points = 1000000
axis_buffer = 1000

initial_state = np.array((initial_x, initial_y, initial_vx, initial_vy))

time = np.linspace(0, runtime, time_points)

def orbitEq(y,t):
    #y = [x,y,x_dot,y_dot]
    g_field = -g*mass_1/(np.sqrt(y[0]**2+y[1]**2))**3
    x_dot = y[2]
    y_dot = y[3]
    x_double_dot = g_field*y[0]
    y_double_dot = g_field*y[1]
    return [x_dot,y_dot,x_double_dot,y_double_dot]

sol_array = odeint(orbitEq, initial_state, time)

fig, ax = plt.subplots()
line, = ax.plot([], [], ".")

def init():
    ax.set_xlim(-1*initial_x -axis_buffer, initial_x + axis_buffer)
    ax.set_ylim(-1 * initial_y - axis_buffer, initial_y + axis_buffer)
    return line,

def update(frame):
    x_points = sol_array[:frame, 0]
    y_points = sol_array[:frame, 1]
    line.set_data(x_points, y_points)
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True)
plt.plot(0,0, "o")
plt.show()

