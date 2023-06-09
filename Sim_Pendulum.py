import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# Set up initial conditions
g = 9.8  # acceleration due to gravity
L = 1.0  # length of pendulum
theta0 = np.pi / 4  # initial angle
omega0 = 0.0  # initial angular velocity

# Set up figure and animation
fig = plt.figure()
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    t = i * 0.05
    theta = theta0 * np.cos(np.sqrt(g / L) * t)
    x = L * np.sin(theta)
    y = -L * np.cos(theta)
    line.set_data([0, x], [0, y])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20)

plt.show()
