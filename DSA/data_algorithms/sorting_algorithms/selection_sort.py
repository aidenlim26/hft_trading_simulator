# Selection Sort
# Time complexity = O(n^2)
# Space complexity = O(1)

array = [-5,3,2,1,-3,-3,7,2,2]

def selection_sort(arr):
    n = len(arr)
    for i in range(0,n):        # Starts at 0 because algo needs to find the very first position to swap the smallest number into
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(array)

print(array)
