import numpy as np
#Create an array of 20 elements containing random integers between 1 and 100.
#Extract only the elements divisible by 5.
#Replace all numbers greater than 80 with -1
random = np.random.default_rng()
array = random.integers(low=1,high=100,size=(1,20))
print(array)
div5 = array[array % 5 == 0]
print(div5)
greater = np.where(array > 80,array,-1)
print(greater)