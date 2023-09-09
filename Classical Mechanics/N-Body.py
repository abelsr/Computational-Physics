# Simulation of N-Body problem using GPU

# Basic libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# GPU libraries
from numba import cuda

# Constants
G = 1e20
dt = 0.01
N = 1000
M = 1e10
L = 2e10
T = 10

# Initial Conditions for N particles
x = np.random.rand(N) * L
y = np.random.rand(N) * L
z = np.random.rand(N) * L
vx = np.random.rand(N) * T
vy = np.random.rand(N) * T
vz = np.random.rand(N) * T
m = np.ones(N) * M / N


# Generate random colors for particles
colors = np.random.rand(N)

# GPU
@cuda.jit
def update(x, y, z, vx, vy, vz, dt, N):
    """update function that updates the position and velocity of each particle

    Args:
    ----
        * x (numpy.ndarray): Array of x positions of particles
        * y (numpy.ndarray): Array of y positions of particles
        * z (numpy.ndarray): Array of z positions of particles
        * vx (numpy.ndarray): Array of x velocities of particles
        * vy (numpy.ndarray): Array of y velocities of particles
        * vz (numpy.ndarray): Array of z velocities of particles
        * dt (float): Time step
        * N (int): Number of particles

    Returns:
    -------
        None

    """
    i = cuda.grid(1)
    if i < N:
        ax = 0
        ay = 0
        az = 0
        for j in range(N):
            if i != j:
                r = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2) ** 0.5
                ax += -G * m[j] * (x[i] - x[j]) / r ** 3
                ay += -G * m[j] * (y[i] - y[j]) / r ** 3
                az += -G * m[j] * (z[i] - z[j]) / r ** 3
        vx[i] += ax * dt
        vy[i] += ay * dt
        vz[i] += az * dt
        x[i] += vx[i] * dt
        y[i] += vy[i] * dt
        z[i] += vz[i] * dt

# Main
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(0, L)
ax.set_ylim3d(0, L)
ax.set_zlim3d(0, L)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
scat = ax.scatter(x, y, z, c=colors, cmap='coolwarm', s=25, vmin=0.5, vmax=1, marker='o', alpha=1)
time_text = ax.text(0.02, 0.95, 0.95, '', transform=ax.transAxes)
plt.title('N-Body Simulation')
# Wait to press enter to start animation, meanwhile show initial conditions
plt.show(block=False)
input('Press enter to start animation')

# Animation
def animate(i):
    global x, y, z, vx, vy, vz, colors
    block_size = 128  # Tamaño de cada bloque
    num_blocks = (N + block_size - 1) // block_size  # Número total de bloques
    update[(num_blocks, ), (block_size, )](x, y, z, vx, vy, vz, dt, N)
    scat._offsets3d = (x, y, z)  # Actualizar posiciones de las partículas
    scat.set_array(colors)
    time_text.set_text('Time = %.1f' % (i * dt))
    return scat, time_text

ani = animation.FuncAnimation(fig, animate, interval=0.1)
plt.show()
