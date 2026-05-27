import numpy as np
#Create an array of 100 random floats between 0 and 1 using np.random.rand().
#Filter only numbers greater than 0.75.
#Calculate the mean of the remaining numbers.
random = np.random.default_rng()
array = random.uniform(low=0,high=1,size=99)
print(array)
print("/")
greater = array[array > 0.75]
print(greater)
print("/")
meangreater = np.mean(greater)
print(meangreater)