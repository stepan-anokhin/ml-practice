import matplotlib.pyplot as plt
import numpy as np
import numpy.random


def helix(radius=5.0, step=5.0, count=1000, noize=0.2):
    """Generate data along a 3D helix."""
    phi = np.random.uniform(0, 2 * np.pi * 10, size=count)
    x = radius * np.cos(phi)
    y = radius * np.sin(phi)
    z = step * phi / (2 * np.pi)
    points = np.dstack([x, y, z])[0] + np.random.normal(0.0, noize, size=(count, 3))
    return points


def scatter3d(data):
    """Show 3D scatter plot."""
    fig = plt.figure(figsize=(8, 8), dpi=80)
    axes = fig.add_subplot(projection="3d")
    axes.scatter(data[:, 0], data[:, 1], data[:, 2], alpha=0.5)
    return fig


scatter3d(helix())
plt.show()
