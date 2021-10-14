import numpy as np

a = [3, 4, 5]
b = [7, 8, 9]

# the dot product can be computed as follows
# 3*7 + 4*8 + 5*9
# 21 + 32 + 45
# = 98

dp = np.dot(a, b)

# returns 98
print(dp)

# the output is always a single scalar value
# If both inputs are scalars, np.dot() will multiply the scalars together and
# output a scalar.
# If one input is a scalar and one is an array, np.dot() will multiply every value
# of the array by the scalar (i.e., scalar multiplication).
# If both inputs are 1-dimensional arrays, np.dot() will compute the dot product
# of the inputs
# If both inputs are 2-dimensional arrays, then np.dot() will perform matrix
# multiplication.
