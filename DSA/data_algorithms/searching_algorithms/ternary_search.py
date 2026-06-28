# Ternary Search
# Inputs must be sorted in asecnding order

array = [2,3,7,8,10,15,21,61,67,99]


def ternary_search_algorithm(array,target):
    return ternary_search_algorithm(array,0,len(array)-1,target)

def ternary_search(array,l,r,target):       #l is very first index, r is last index
    while l <= r:
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) // 3

        if target == array[mid1]:
            return mid1
        if target == array[mid2]:
            return mid2
        
        if target < array[mid1]:    # target is on the left side of the mid
            r = mid1 - 1
        elif target > array[mid2]:  # target is on the right side of the mid
            l = mid2 + 1
        else:
            # Target is between mid1 and mid2
            l = mid1 + 1
            r = mid2 - 1
    return -1

print(ternary_search(array, 0, len(array) - 1, 111))

