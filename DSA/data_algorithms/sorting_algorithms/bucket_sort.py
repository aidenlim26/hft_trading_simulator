# Bucket Sort
# Can't have -ve numbers in the input

array = [5,3,2,1,3,3,7,2,2]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):         # j is decrementing (-ve)
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return arr
    
    # Create empty buckets
    buckets = []
    for i in range(n):
        buckets.append([])

    # Part 1: Normalise & place into buckets
    max_value = max(arr)
    for num in arr:
        normalised = num / (max_value + 1)
        bucketNumber = int(n * normalised)
        buckets[bucketNumber].append(num)

    # Part 2: Sort each bucket
    for bucket in buckets:
        insertion_sort(bucket)
    
    # Part 3: Combine sorted buckets
    output = []
    for bucket in buckets:
        output.extend(bucket)
    return output

print(bucket_sort(array))