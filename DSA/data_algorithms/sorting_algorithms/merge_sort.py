# Merge Sort
# Time complexity = O(n log n)
# Space complexity = O(n)

array = [-5,3,2,1,-3,-3,7,2,2]

def merge_sort(arr):
    n = len(arr)


    if n == 1:              # Basically uses recursion to split up the array until each array has only 1 value
        return arr
    
    m = len(arr) // 2       # m is the middle index, use "//" to do floor division (lower integer of the float)
    L = arr[:m]             # Left side is all the values index up till the middle (doesn't include m)
    R = arr[m:]             # Right side "m" + all the values to the right

    L = merge_sort(L)       # Uses recursion to sort itself (L & R)
    R = merge_sort(R)
    l, r = 0,0              # Initialising
    L_len = len(L)
    R_len = len(R)

    sorted_array = [0] * n  # Creating a new array to merge sorted arrays
    i = 0                   # Initialising "i"


# MERGING (FOR BOTH INDIVIDUAL VALUE ARRAYS AND THE 2 MAIN ARRAYS)
    while l < L_len and r < R_len:
        if L[l] < R[r]:                 #Comparing values
            sorted_array[i] = L[l]
            l += 1                      # Increment l
        else:
            sorted_array[i] = R[r]
            r += 1
        
        i += 1      # Increment to move onto the next index

# To sweep up the last values and add it to the sorted array
    while l < L_len:
        sorted_array[i] = L[l]
        l += 1
        i += 1

    while r < R_len:
        sorted_array[i] = R[r]
        r += 1
        i += 1

    return sorted_array

print(merge_sort(array))
