# Jump Search
# Input must be sorted in ascending order


numbers = [10,20,30,40,50]
target = 10

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))                 # Determines the jump step
    prev = 0 
    while arr[min(n,step)-1] < target:       # Stops the while loop after the jump step overshoots the target, finds the smaller value between n and step, "-1" is due to array indexing
        prev = step
        step = step + int(math.sqrt(n))      # "step" increases every loop, which is why it isn't step + step, but instead step + (original step formula)
        if prev >= n:                        # If search goes "out of bounds" returns -1
            return -1
    for i in range(prev, min(step,n)):       # Linear search
        if target == arr[i]:
            return i
    return -1

result = jump_search(numbers,target)

if result != -1:
    print(f"{target} is found at index: {result}")
else:
    print(f"{target} is not found")


        