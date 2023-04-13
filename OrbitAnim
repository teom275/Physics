import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define parameters
m1 = 5.0  # mass of object 1
m2 = 5.0  # mass of object 2
G = 1.0   # gravitational constant
dt = 0.01 # time step
num_steps = 1000 # number of time steps

# Initial conditions
x1 = 0.0  # initial x-coordinate of object 1
y1 = 0.0  # initial y-coordinate of object 1

x2 = 1.0  # initial x-coordinate of object 2
y2 = 0.0  # initial y-coordinate of object 2

# Calculate the distance between the objects
r = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Set initial velocities
vx1 = 0.0
vy1 = 10

vx2 = 0.0
vy2 = -10

# Arrays to store the coordinates of the objects at each time step
x1_vals = []
y1_vals = []
x2_vals = []
y2_vals = []

# Euler method for numerical integration
for step in range(num_steps):
    # Store the current coordinates of the objects
    x1_vals.append(x1)
    y1_vals.append(y1)
    x2_vals.append(x2)
    y2_vals.append(y2)
    
    # Update the velocities of the objects
    vx1 += G * m2 * (x2 - x1) / r**3 * dt
    vy1 += G * m2 * (y2 - y1) / r**3 * dt
    vx2 += G * m1 * (x1 - x2) / r**3 * dt
    vy2 += G * m1 * (y1 - y2) / r**3 * dt
    
    # Update the coordinates of the objects
    x1 += vx1 * dt
    y1 += vy1 * dt
    x2 += vx2 * dt
    y2 += vy2 * dt

# Convert the lists to arrays for plotting
x1_vals = np.array(x1_vals)
y1_vals = np.array(y1_vals)
x2_vals = np.array(x2_vals)
y2_vals = np.array(y2_vals)

# Create a figure and axes for the plot
fig, ax = plt.subplots()

# Set up the plot with initial data
orbit1, = ax.plot(x1_vals, y1_vals, label='Object 1')
orbit2, = ax.plot(x2_vals, y2_vals, label='Object 2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Circular Orbit of Object 1 around Object 2')
ax.legend()
ax.grid()
ax.axis('equal')

# Animation update function
def update(frame):
    # Update the data for the plot
    orbit1.set_data(x1_vals[:frame+1], y1_vals[:frame+1])
    orbit2.set_data(x2_vals[:frame+1], y2_vals[:frame+1])

# Create the animation
animation = FuncAnimation(fig, update, frames=num_steps, interval=10)

# Save the animation as an animated GIF using Pillow writer
animation.save('orbit.gif', writer='pillow')


