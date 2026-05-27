import numpy as np
#Create a 1D array of 50 random numbers.
#Find the mean, median, standard deviation, and variance.
random = np.random.default_rng()
arr = random.integers(1,100,size=(5,10))
print(arr)
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)
var = np.var(arr)
print(mean)
print(median)
print(std)
print(var)
