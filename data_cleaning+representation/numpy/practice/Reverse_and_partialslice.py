import numpy as np
#Using slicing only, reverse the rows and return only the last two columns.
d = np.array([[10, 20, 30, 40],
              [50, 60, 70, 80],
              [90, 100, 110, 120]])
reverse = d[::-1,2:]
print(reverse)

