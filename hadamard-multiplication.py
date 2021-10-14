import numpy as np

# also called element wise
# both vectors need to be the same size

w1 = [1, 3, 5]
w2 = [3, 4, 2]

w3 = np.multiply(w1, w2)

# [ 3, 12, 10]
print(w3)
