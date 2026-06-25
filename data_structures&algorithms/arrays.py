# Arrays can be fixed or dynamic sized.
# At the very core of it, accessing our arrays is accessing a specific memory in your RAM. 
# Accessing an index of an array is the same process no matter how large the array is which is why it's big O notation is O(1)


# FIXED SIZED ARRAYS - Need to decide size of array when initialising
# Inserting a value into an array forces all the latter indexes to shift to the right by 1, which is why it's big O notations is O(n).
# However, if it's getting inserted second to the end, only the last index needs to shift by 1 everytime, which is why its O(1).
# Same logic for deleting an index


# DYNAMIC SIZED ARRAYS
# At it's core, all arrays are fixed. However, when implementing a dynamic sized array, a new fixed array is created of a different size.
# Values from old array are just copied into the new array and new values are added


# Big O Notation for Arrays:
# Initialisation: O(n)
# Insertion: O(n)
# Deletion: O(n)
# Index Access: O(1)
# Append: O(1)
# Pop: O(1)