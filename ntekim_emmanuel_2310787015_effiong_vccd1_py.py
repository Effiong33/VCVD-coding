import matplotlib.pyplot as plt
import numpy as np

def braking_distance(initial_velocity, deceleration):
    braking_distance = (initial_velocity ** 2) / (2 * deceleration)
    return braking_distance

def velocity_time_graph(initial_velocity, deceleration, time_interval):
    time_points = np.arange(0, time_interval + 0.1, 0.1)
    velocities = initial_velocity - deceleration * time_points
    return time_points, velocities

def distance_time_graph(initial_velocity, deceleration, time_interval):
    time_points = np.arange(0, time_interval + 0.1, 0.1)
    distances = initial_velocity * time_points - 0.5 * deceleration * time_points**2
    return time_points, distances

# Take user inputs with validation
try:
    initial_velocity = float(input("Enter the initial velocity of the vehicle (m/s): "))
    deceleration = float(input("Enter the deceleration or braking acceleration (m/s^2): "))
except ValueError:
    print("Invalid input. Please enter numerical values where required.")
    exit()

time_interval = 10.0  # seconds

# Calculate braking distance
distance = braking_distance(initial_velocity, deceleration)
print(f"The braking distance is: {distance} meters")

# Velocity-time graph
time_points, velocities = velocity_time_graph(initial_velocity, deceleration, time_interval)
plt.subplot(2, 1, 1)
plt.plot(time_points, velocities, label='Velocity')
plt.title('Velocity-Time Graph')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()

# Distance-time graph
time_points, distances = distance_time_graph(initial_velocity, deceleration, time_interval)
plt.subplot(2, 1, 2)
plt.plot(time_points, distances, label='Distance')
plt.title('Distance-Time Graph')
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.legend()

plt.tight_layout()
plt.show()
