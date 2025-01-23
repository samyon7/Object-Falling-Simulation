import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
g = 90.81  # Acceleration due to gravity (m/s^2)
h0 = 1000.0  # Initial height (m)
v0 = 0.0  # Initial velocity (m/s)
dt = 0.01  # Time step (s)
T = 10.0  # Total simulation time (s)

# Time array
time = np.arange(0, T, dt)

# Calculate position, velocity, and acceleration
h = h0 + v0 * time + 0.5 * (-g) * time**2
v = v0 + (-g) * time
a = -g  # Constant acceleration

# Find the time when the ball hits the ground
t_ground = np.sqrt(2 * h0 / g)

# Adjust T if the ball hits the ground before T
if t_ground < T:
    T = t_ground
    time = np.arange(0, T, dt)
    h = h0 + v0 * time + 0.5 * (-g) * time**2
    v = v0 + (-g) * time

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(0, h0 + 1)
ax.set_title('Ball Falling with Velocity Visualization')
ax.set_xlabel('Position (m)')
ax.set_ylabel('Height (m)')
ax.grid(True)

# Initialize a circle for the ball
ball_radius = 0.1
ball = plt.Circle((0, h0), ball_radius, color='blue')
ax.add_patch(ball)

ground, = ax.plot([-1, 1], [0, 0], color='green', linewidth=2)

# Initialize a quiver for velocity vectors
quiver = ax.quiver(0, h0, 0, v0, color='red', scale=50, scale_units='xy', width=0.005, headwidth=3, headlength=40)

# Initialize text to display current velocity
velocity_text = ax.text(-0.8, h0, f'Velocity: {v0:.2f} m/s', fontsize=9, color='red')

# Animation function
def animate(i):
    # Update the ball's position
    ball.center = (0, h[i])
    
    # Update the velocity vector
    quiver.set_offsets([0, h[i]])
    quiver.set_UVC(0, v[i])
    
    # Update the velocity text
    velocity_text.set_position((-0.8, h[i]))
    velocity_text.set_text(f'Velocity: {v[i]:.2f} m/s')
    
    return ball, quiver, velocity_text,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(time), interval=10, blit=True, repeat=False)
ani.save('object_falling.mp4', writer=writer)
plt.show()
