import numpy as np
#Given a 3×4 NumPy array of integers,
#subtract the mean of each row from the elements in that row.

array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])
print(array.shape)
mean = np.mean(array,axis=1)
print(mean)
reshapemean = mean.reshape(-1,1) #reshape into a column vector
print(reshapemean)
array1 = array - reshapemean
print(array1)
