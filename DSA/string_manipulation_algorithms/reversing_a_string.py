str = "welcome to python programming"

words = str.split(" ")
print(words)    #['welcome', 'to', 'python', 'programming']

words = words[-1::-1]   # list[start:stop:step], -1 is the last index 
print(words)    #['programming', 'python', 'to', 'welcome']

outputstr = ' '.join(words)     # ' ' is the connector between the values in the list

print(outputstr)