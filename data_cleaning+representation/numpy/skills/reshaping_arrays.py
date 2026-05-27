import numpy as np
#ARRAYS CAN ONLY BE RESHAPED TO ANOTHER DIMENSION WITH THE SAME AMOUNT OF ELEMENTS
arr = np.arange(6) #Print range as an array
print(arr)
reshaped = arr.reshape(2,3)
print(reshaped)

columnvector = reshaped.reshape(-1,1)  #To reshape any array into a singular column
print(columnvector)

rowvector = reshaped.reshape(1,-1)     #To reshape any array into a singular row
print(rowvector)