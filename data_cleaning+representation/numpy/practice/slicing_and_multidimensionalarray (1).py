import numpy as np
b = np.arange(1, 17).reshape(4, 4)
print(b)

#slice b to get the middle 2x2 block

slice = b[1:3,1:3]
print(slice)