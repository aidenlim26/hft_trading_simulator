import numpy as np
#Generate a 5×5 random matrix of integers between 1–10.
#Find the sum of all elements.
#Compute the mean of each row (axis=1) and each column (axis=0).
random = np.random.default_rng()
array = random.integers(low=1,high=10,size=(5,5))
sum = np.sum(array)
meanrow = np.mean(array,axis=1)
meancolumn = np.mean(array,axis=0)
print(array)
print(sum)
print(meanrow)
print(meancolumn)
