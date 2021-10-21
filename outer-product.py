import numpy as np

# v = [1, 2, 3]
# w = [4, 5, 6]

# Dot Product = v'w
# the result of the dot product is always a single number regardless of vector
# sizes

# Outer Product = vw'
# the result of the outer product is not a single number, it is a matrix
# unlike the dot product the outer product can be computed from vectors that
# have different lengths

# the outer product
# | 1 | * | a b c d | = | 1a 1b 1c 1d |
# | 0 |                 | 0a 0b 0c 0d |
# | 2 |                 | 2a 2b 2c 2d |
# | 5 |                 | 5a 5b 5c 5d |

v1 = np.array([1, 2, 3])
v2 = np.array([-1, 0, 1])

# in this example
# | 1 | * | -1 0 1 | = | -1 0 1 |
# | 2 |                | -2 0 2 |
# | 3 |                | -3 0 3 |

# outer product
v3 = np.outer(v1, v2)
print(v3)
