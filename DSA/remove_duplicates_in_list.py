#Write a program to remove the duplicates in a list

numbers = [0,1,2,3,3,4,5,5,6,7,8,8]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

uniques.sort()
print(uniques)
