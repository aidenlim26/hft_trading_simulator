import numpy as np
#Generate a 4×4 matrix of random integers from 0–50.
#Find the maximum value, minimum value, and their positions (indices).

random = np.random.default_rng()

array = random.integers(0,51,size=(4,4))
print(array)
max = np.max(array)
min = np.min(array)
argmax = np.argmax(array)
argmin = np.argmin(array)
print(max)
print(min)
print(argmax)
print(argmin)