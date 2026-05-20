NumberGenerated = [[0]*101 for i in range(2)]

import random

namearray = [0,0]

NumberGenerated[0][0] = "Player 1"
NumberGenerated[1][0] = "Player 2"

for i in range(1,101):
    NumberGenerated[0][i]= random.randint(1,6)
    NumberGenerated[1][i] = random.randint(1,6)

for count in range(2):
    name = str(input("Enter your first name: "))
    if len(name) == 0 or len(name) > 12:
        print("Please enter a valid name")
    else:
        namearray[count] = name


p1total = 0
p2total = 0

for i in range(1,100):
    if NumberGenerated[0][i] > NumberGenerated[0][i+1]:
        p1total = p1total + 2
    elif NumberGenerated[0][i] == NumberGenerated[0][i+1]:
        p1total = p1total + 1
        p2total = p2total + 1
    else: 
        p2total = p2total + 2

if p1total > p2total:
    print("Name: ", namearray[0])
    print("Total points: ", p1total)
elif p2total > p1total:
    print("Name: ", namearray[1])
    print("Total points: ", p2total)
else:
    equal = True
    while equal == True:
        p1additional = random.randint(1,6)
        p2additional = random.randint(1,6)
        if p1additional > p2additional:
            p1total = p1total + 2
            print("Name: ", namearray[1])
            print("Total points: ", p2total)
            equal == False
        elif p2additional > p1additional:
            p2total = p2total + 2
            print("Name: ", namearray[1])
            print("Total points: ", p2total)
            equal == False

        



