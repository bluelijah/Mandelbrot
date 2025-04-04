import numpy as np
import matplotlib.pyplot as plt
import time

# The mandelbrot fractal is an infinite fractal that plots the equation Zn+1 = Zn ^ 2 + c
# c is the constant that determines how the complex numbers of i grow under iteration
# If Zn remains bounded, then this is part of the mandelbrot set, and goes to black
# If Zn is unbounded, then it escapes to infinity and lies outside of the mandelbrot set

def mandelbrot(c, maxIterations):
    z = 0
    for n in range(maxIterations):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return maxIterations

def generateSet(xmin, xmax, ymin, ymax, width, height, maxIterations):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mandelbrot_set = np.zeros((height, width))
    
    for i in range(height):
        for j in range(width):
            c = x[j] + 1j * y[i]
            mandelbrot_set[i, j] = mandelbrot(c, maxIterations)
    return mandelbrot_set

# Initial area of the Mandelbrot set (zooming near the edge)
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
zoom_factor = 0.7  # Adjust the zoom factor for smoother zooming
width, height = 400, 400  # Reduce resolution to speed up rendering
maxIterations = 400  # Reduce iterations for faster rendering

def graphFractal():
    global xmin, xmax, ymin, ymax
    plt.clf()
    fig = plt.gcf()
    fig.patch.set_facecolor('black')  # Background color for the entire figure
    ax = plt.gca()
    ax.set_facecolor('black')  # Background color for the plot area
    
    mandelbrot_set = generateSet(xmin, xmax, ymin, ymax, width, height, maxIterations)
    img = plt.imshow(
        mandelbrot_set,
        extent=[xmin, xmax, ymin, ymax],
        cmap="magma",
        interpolation="bilinear"
    )
    
    # Purple border box
    ax.add_patch(plt.Rectangle(
        (xmin, ymin),
        xmax - xmin,
        ymax - ymin,
        edgecolor='purple',
        facecolor='none',
        linewidth=2
    ))

    plt.colorbar(img, label="Iterations")
    
    plt.title("Mandelbrot Set", color='white')
    plt.xlabel("Real Parts", color='white')
    plt.ylabel("Imaginary Parts", color='white')
    ax.tick_params(colors='white')  # Set axis tick color to white

    # Display scale measurement in top-right corner (text only)
    x_range = xmax - xmin
    scale_length = x_range * 0.2
    x_text = xmax - 0.25 * x_range
    y_text = ymax - 0.07 * (ymax - ymin)
    plt.text(x_text, y_text, f"Scale: {scale_length:.2e}", color="white", fontsize=12)
    
    plt.draw()

def zoomIn():
    global xmin, xmax, ymin, ymax
    # Instead of zooming in the center, choose an edge of the set
    x_center, y_center = -0.585, -0.447  #ZOOM LOCATION
    
    for _ in range(30):  # Zoom in 30 times (fewer zooms)
        # Decrease the ranges for zooming
        x_range = (xmax - xmin) * zoom_factor
        y_range = (ymax - ymin) * zoom_factor
        xmin, xmax = x_center - x_range / 2, x_center + x_range / 2
        ymin, ymax = y_center - y_range / 2, y_center + y_range / 2

        graphFractal()
        plt.pause(0.1)  # Pause for 100 milliseconds for smooth animation

# Initialize the plot
fig, ax = plt.subplots()

# Begin the zoom animation
zoomIn()

plt.show()