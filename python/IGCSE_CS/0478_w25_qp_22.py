Random_Number = [0]* 100000
CountedNumber = [[0]*2 for i in range(10)]

import random

for count in range(100000):
    Random_Number[count] = random.randint(1,10)

for count in range(10):
    CountedNumber[count][0] = count
    CountedNumber[count][1] = 0

for i in range(10):
    for j in range(100000):
        if Random_Number[j] == CountedNumber[i][0]:
            CountedNumber[i][1] = CountedNumber[i][1] + 1

swap = True
while swap == True:
    swap = False
    for i in range(9):
        if CountedNumber[i+1][1] > CountedNumber[i][1]:
            temp1 = CountedNumber[i][1]
            temp2 = CountedNumber[i+1][1]
            CountedNumber[i][1] = temp2
            CountedNumber[i+1][1] = temp1
            swap = True


def chance(value):
    chance = value / 100000
    return chance

for i in range(10):
    print(CountedNumber[i][0])
    print("Chance of generating this number: ", chance(CountedNumber[i][1]))
