import numpy as np

#Scalar arithmetic

#array = np.array([1,2,3])
#print(array + 1)
#print(array -2)
#print(array * 3)
#print(array / 4)
#print(array ** 5) #The power operator is "**", so its outputting array to the power of 5

#Vectorised math functions

#array = np.array([1,2,3])
#print(np.sqrt(array))
#print(np.round(array))
#print(np.pi)


#Excercise: find area of a circle with given radius
#radius = np.array([1,2,3,4,5])
#print(np.pi*(radius**2))

#Element-wise arithmetic (applying operations between single elements between two arrays)

#array1 = np.array([1,2,3])
#array2 = np.array([4,5,6])
#print(array1+array2)
#print(array1-array2)
#print(array1*array2)
#print(array1/array2)
#print(array1**array2)

#Comparison operators

scores = np.array([91,55,100,73,82,64])
#print(scores == 100)
#print(scores >= 60)
#print(scores < 60)

scores[scores < 60] = 0
print(scores)


