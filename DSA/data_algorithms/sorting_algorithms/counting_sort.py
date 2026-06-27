# Counting Sort
# Time complexity = O(n + k) where k is the range of data

# Note - This can be written with negative arrays, but we'll stick to positive arrays,
# so k is the max of the array

# Space complexity = O(k)

array = [5,3,2,1,3,3,7,2,2]

def counting_sort(arr):
    n = len(arr)
    maxx = max(arr)
    counts = [0] * (maxx + 1)

    for x in arr:
        counts[x] += 1              # Concatenates the index for the counts

    i = 0

# SORTING THE ARRAY
    for c in range(maxx+1):         # Go through all valid positions until maxx
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1

counting_sort(array)

print(array)