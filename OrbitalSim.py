import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

axesLength = 7500

G = 6.67430e-20  # Gravitational constant in km^3 kg^(-1) s^(-2)
m1 = 5.97219e24  # Mass of the first body (e.g., Earth) in kg
m2 = 1000       # Mass of the second body in kg
mu = G * m1     # Gravitational parameter

r0 = np.array([1500, 0, 0])  # Initial position vector
v0 = np.array([0, 18, 0])        # Initial velocity vector
y0 = np.hstack((r0, v0))        # Initial state vector

def two_body(t, y):
    r = y[:3]
    v = y[3:]
    r_mag = np.linalg.norm(r)
    a = -mu * r / r_mag**3
    return np.hstack((v, a))

t_span = (0, 10000)  # Time span for the simulation
t_eval = np.linspace(t_span[0], t_span[1], 10000)
sol = solve_ivp(two_body, t_span, y0, t_eval=t_eval)

Y = sol.y.T
x, y, z = Y[:, 0], Y[:, 1], Y[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X-axis (km)')
ax.set_ylabel('Y-axis (km)')
ax.set_zlabel('Z-axis (km)')

# Initialize an empty line for the animation
line, = ax.plot([], [], [], 'o-', markersize=8)
small_sphere = ax.scatter([], [], [], color='blue', marker='o', s=50, label='Smaller Body')

# Animation update function
def update(frame, x, y, z, line, small_sphere):
    line.set_data(x[frame], y[frame])
    line.set_3d_properties(z[frame])
    return line, small_sphere

ax.set_xlim(-axesLength, axesLength)
ax.set_ylim(-axesLength, axesLength)
ax.set_zlim(-axesLength, axesLength)


ax.scatter(0, 0, 0, color='red', marker='o', s=500, label='Larger Body')


# Set up the animation
animation = FuncAnimation(fig, update, frames=len(t_eval), fargs=(x, y, z, line, small_sphere), interval=50, blit=False, repeat=True)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(False)
plt.show()
