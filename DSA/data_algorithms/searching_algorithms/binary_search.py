# Binary Search
# Inputs must be in ascending order

numbers = [23,24,25,26,27,28,29,30,31]
find = 25
found = False
startIndex = 0
endIndex = len(numbers) - 1

while startIndex <= endIndex:
    midpoint = (endIndex + startIndex) // 2     # floor division (round down)

    if numbers[midpoint] == find:
        print(f"Found at: {midpoint}")
        found = True
        break

# Creating the new range to search
    if numbers[midpoint] > find:
        endIndex = midpoint - 1
    else:
        startIndex = midpoint + 1

if not found:
    print("Not found")