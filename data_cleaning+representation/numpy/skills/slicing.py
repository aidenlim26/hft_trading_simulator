import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# array[start:end:step]
# "end" is exclusive so if u wna get the 3rd index u have to write :4
# using ":" means you are selecting the entire row / column depending on where you place it
# the array format is [row,column], or [y,x]

print(array[1:4,1:3])

