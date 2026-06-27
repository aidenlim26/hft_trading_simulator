# Bubble Sort
# Time complexity = O(n^2)
# Space complexity = O(1)

array = [-5,3,2,1,-3,-3,7,2,2]

def bubble_sort(arr):       # arr is a self-named variable, not a keyword
    n = len(arr)
    flag = True

    while flag == True:
        flag = False        # Auto set flag to False so that the program stops when there's nothing to sort
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                flag = True     # Set flag to True so that the program loops again
                arr[i-1], arr[i] = arr[i], arr[i-1]     # Unpacking method

bubble_sort(array)

print(array)