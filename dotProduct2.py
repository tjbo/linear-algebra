import numpy as np

# is the dot product is commutative?
a = np.random.randn(100)
b = np.random.randn(100)

# compute dps, (we do not need to transpose as py flips one vector to column automatically)
dp_ab = np.dot(a, b)
dp_ba = np.dot(b, a)

print(dp_ab == dp_ba)
