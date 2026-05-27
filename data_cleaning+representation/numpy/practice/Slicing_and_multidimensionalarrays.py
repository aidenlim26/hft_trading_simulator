import numpy as np
#Make a 5×5 array with numbers 1–25 using np.arange().
#Extract the center 3×3 subarray using slicing.
#Replace the border values of the 5×5 array with 0s.
arr = np.arange(1,26).reshape(5,5)
print(arr)
center = arr[1:4,1:4]
print(center)
arr[0,:] = 0
arr[:,0] = 0
arr[:,4] = 0
arr[4,:] = 0
print(arr)