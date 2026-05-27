import numpy as np

random = np.random.default_rng()

#print(random.integers(low=1,high=101,size=3))   #The first 2 numbers inside integers() is the range. The second number is exclusive
                                                 #The "size" is the amount of numbers it generates

#print(random.integers(low=1,high=101,size=(3,2)))       #You can make the size into an array but setting the dimensions, in this case it is (3,2) = 3 rows, 2 columns

#If you want to reproduce the same results you need to set a seed
#random1 = np.random.default_rng(seed=1)
#np.random.seed(seed=1)

#print(np.random.uniform(low=-1,high=1,size=(3,2)))  #Uniform = uniform distribution means each value has an equal chance of being selected

#How to shuffle an array
rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
fruits = np.array(["apples","oranges","banana","coconut","pineapple"])
fruit = rng.choice(fruits,size=(3,3)) #"rng.choice()" is to randomly select a value from the array
rng.shuffle(array)
print(array)
print(fruits)
print(fruit)