import numpy as np
#Given a 4×4 matrix, extract:
#Every even-indexed row.
#Every odd-indexed column.
matrix = np.arange(1,17).reshape(4,4)
print(matrix)
even_rows = matrix[::2,:]
odd_columns = matrix[:,1::2]
print(even_rows)
print(odd_columns)