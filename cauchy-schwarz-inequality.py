import numpy as np

# these are not proofs, just a way to internalize concepts

# create 3 vectors, one of which is dependent on the other
a = np.random.randn(5)
b = np.random.randn(5)

# this will create a linearly dependent set
c = np.random.randn(1) * a

# compute dot products
aTb = np.dot(a, b)
aTc = np.dot(a, c)

# the norm of a vector, aka vector length or magnitude
aNb = np.linalg.norm(a) * np.linalg.norm(b)
aNc = np.linalg.norm(a) * np.linalg.norm(c)

# demonstrate the inequalities
print(f"{aTb}, {aNb}")

# demonstrate the equality, (linear dependence)
print(f"{aTc}, {aNc}")
