import numpy as np
#Extract the second row ([4, 5, 6]) using slicing.
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(array[1,:])

#Using the same array a,
#Q: Extract the first and second columns (i.e., all rows, columns 0 and 1).
print(array[:,:2])