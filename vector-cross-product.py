import numpy as np
import matplotlib.pyplot as plt

# the vector cross product
# used only for when you have two 3d vectors
# result is another 3d vector

# | 1 | * | a | = | 2c - 3b |
# | 2 |   | b |   | 3a - 1c |
# | 3 |   | c |   | 1b - 2a |

v1 = [-3, 2, 5]
v2 = [4, -3, 0]

v3 = np.cross(v1, v2)

fig = plt.figure()
ax = fig.gca(projection="3d")

print(v3)

xx, yy = np.meshgrid(np.linspace(-10, 10, 10), np.linspace(-10, 10, 10))
z1 = (-v3[0] * xx - v3[1] * yy) / v3[2]
ax.plot_surface(xx, yy, z1)

# plot the vectors
ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], "k")
ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], "k")
ax.plot([0, v3[0]], [0, v3[1]], [0, v3[2]], "k")

ax.view_init(azim=150, elev=45)
plt.show()
