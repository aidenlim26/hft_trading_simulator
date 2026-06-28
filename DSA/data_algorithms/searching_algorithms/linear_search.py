numbers = [4,2,46,8,1,13,6,58,10]
find = 10
found = False
count = 1

for i in numbers:
    if i == find:
        found = True
        print("Found at position", count)

    else:
        count = count + 1

if not found:                       # Takes the last value that has already been checked by the loop
    print("Item not found")
