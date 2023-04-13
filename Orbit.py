import matplotlib.pyplot as plt
import numpy as np

# Constants
G = 6.67e-11  # Gravitational constant
M = 1.989e30  # Mass of the sun

# Initial conditions
r0 = 1.6e11  # Initial distance from the sun
v0 = 29.3e3  # Initial velocity

# Time step
dt = 8640  # One day

# Calculate position and velocity of the body as a function of time
r = r0
v = v0
t = 0
positions = [(r0, 0)]
while r > 0:
    a = -G * M / r**2  # Acceleration
    v += a * dt  # Velocity
    r += v * dt  # Position
    t += dt
    positions.append((r, t))

# Plot the orbit
positions = np.array(positions)
plt.plot(positions[:, 0], positions[:, 1])
plt.show()
