import numpy as np
#Given a 3×3 matrix of any numbers, subtract the mean of each column from that column using broadcasting.
array = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
columnmean = np.mean(array,axis=0)
print(array)
print("The mean of each column:",columnmean)
array1 = (array - columnmean)
print(array1)
print(array1.shape)