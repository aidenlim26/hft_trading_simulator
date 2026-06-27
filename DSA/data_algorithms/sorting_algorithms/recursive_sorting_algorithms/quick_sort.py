# Quick Sort
# Time complexity: O(n log n) (Average case, technically worst case if O(n^2))
# Space complexity: O(n)
# Quick sort splits array up into 3 pieces, (Smaller than pivot), pivot, (larger than pivot)

array = [-5,3,2,1,-3,-3,7,2,2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr          # For base cases, if the array is already sorted
    
    pivot = arr[-1]         # Make the last value the pivot

# Creating the left & right arrays
    L = [x for x in arr[:-1] if x <= pivot] 
    R = [x for x in arr[:-1] if x > pivot]

    L = quick_sort(L)
    R = quick_sort(R)

# Concatenating the left & right arrays as well as the 2 main + pivot
    return L + [pivot] + R      # Pivot is converted into a list so that it can concat w/ L & R

quick_sort(array)

print(array)

