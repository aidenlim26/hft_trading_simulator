import numpy as np
#Given this array:
arr = np.array([[10, 15, 20],
                [25, 30, 35],
                [40, 45, 50]])
#Filter all elements greater than or equal to 30.
#Replace them with their value divided by 10.
greaterequal = np.where(arr >= 30,arr,(arr/10) )
print(greaterequal)
