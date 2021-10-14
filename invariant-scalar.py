import numpy as np

# test whether the dot product sign is invariant to scalar multiplication

# generate 2 vectors {R3}
a = [-3, 4, 6]
b = [3, 6, -3]

# generate 2 scalars
s1 = 2
s2 = 4

dp1 = np.dot(a, b)
dp2 = np.dot(np.multiply(a, s1), np.multiply(b, s2))

# the scaled dp version is 6x bigger
# returns -3, 18
print(dp1, dp2)

# scalar mutliplication has an effect on the dot product
