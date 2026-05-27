import numpy as np
#Q: Use slicing to get every second element starting from index 1.
array = np.arange(10)
slice = array[1::2]
print(slice)