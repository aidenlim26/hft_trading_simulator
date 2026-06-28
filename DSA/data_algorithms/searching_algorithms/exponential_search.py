# Exponential Search
# Input must be pre-sorted in ascending order

def binary_search(arr, low, high, target):
    """Standard binary search to precisely locate the target within a range."""
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return -1


def exponential_search(arr, target):
    n = len(arr)
    
    # Base Case: Check if the target is at the very first element
    if n == 0:
        return -1
    if arr[0] == target:
        return 0
        
    # Phase 1: Find the exponential range by doubling 'bound'
    bound = 1
    while bound < n and arr[bound] < target:
        bound = bound * 2
        
    # Phase 2: Perform Binary Search on the isolated window
    # Lower bound is the previous step (bound // 2)
    # Upper bound is the smaller value between the current bound or the end of the array
    return binary_search(arr, bound // 2, min(bound, n - 1), target)


# --- Execution Block ---
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 40

result = exponential_search(numbers, target)

if result != -1:
    print(f"{target} is found at index: {result}")
else:
    print(f"{target} is not found")