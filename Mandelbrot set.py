import numpy as np
import matplotlib.pyplot as plt

# Function to check if a point is in the Mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    return n

# Parameters for the complex plane grid
xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5
width, height = 2000, 2000

# Create the grid in the complex plane
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)

# Parameters for the Mandelbrot set
max_iter = 150
threshold = 20

# Calculate the Mandelbrot set
C = X + 1j * Y
mandelbrot_set = np.vectorize(mandelbrot)(C, max_iter)

# Plot the Mandelbrot set
plt.imshow(mandelbrot_set, extent=(xmin, xmax, ymin, ymax), cmap='hot', interpolation='bilinear', origin='lower')
plt.colorbar()
plt.title('Mandelbrot Set')
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()
