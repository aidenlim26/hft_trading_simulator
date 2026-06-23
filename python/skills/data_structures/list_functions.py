numbers = [5,2,1,7,4]

#APPEND
numbers.append(20)
#print(numbers)

#INSERT
numbers.insert(0,10)   # "0" is the position of insert, "10" is the value that is being inserted
#print(numbers)

#REMOVE
numbers.remove(5)      # "5" is the value of the item you want to remove and not the position
#print(numbers)

#CLEAR
#numbers.clear()       # To remove everything in the list
#print(numbers)

#POP
numbers.pop()          # To remove the last value in the list
#print(numbers)

#INDEX
#print(numbers.index(10)) #Prints the position/index of the first occurence of the value(10)
#print(50 in numbers)     #Prints a Boolean value, either T/F to prevent the program from crashing when theres no 50 in the list

#COUNT
#print(numbers.count(10))   #Prints the number of occurences of the value(10) in the list

#SORT
numbers.sort()         # Sorts my list in ascending order
#print(numbers)
numbers.reverse()      # Sorts my list in descending order
#print(numbers)

#COPY
numbers2 = numbers.copy()   # Duplicates the list