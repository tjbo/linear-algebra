import numpy as np

v1 = [1, 2, 3, 4, 5, 6]

# the square root of the dot product of the vector with it self gives us the length
vl1 = np.sqrt(sum(np.multiply(v1, v1)))

# we can just use this built-in in python
vl2 = np.linalg.norm(v1)

print(vl1, vl2)
