import matplotlib.pyplot as plt
import numpy as np

def plot_waves(wave1, wave2, initial_position1=0, initial_position2=0):
    # Create time array
    t = np.arange(0, len(wave1))
    
    # Shift waves by initial position
    wave1 = np.roll(wave1, initial_position1)
    wave2 = np.roll(wave2, initial_position2)
    
    # Plot waves
    plt.plot(t, wave1, label='Wave 1')
    plt.plot(t, wave2, label='Wave 2')
    
    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Oscillation of Two Waves')
    
    # Show legend
    plt.legend()
    
    # Show plot
    plt.show()

# Define wave data
wave1 = np.sin(np.arange(0, 10, 0.1))
wave2 = np.cos(np.arange(0, 10, 0.1))

# Plot waves with initial positions
plot_waves(wave1, wave2, initial_position1=5, initial_position2=10)
