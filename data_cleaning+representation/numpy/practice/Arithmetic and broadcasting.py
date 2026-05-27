import numpy as np
#1.Create an array A with values [1, 2, 3, 4].
    #Multiply the entire array by 5 using broadcasting.
    #Create another array B = [10, 20, 30, 40] and compute A + B and A * B.
A = np.array([1,2,3,4])
print(A*5)
B = np.array([10,20,30,40])
sum = (A+B)
product = (A*B)
print(sum)
print(product)
