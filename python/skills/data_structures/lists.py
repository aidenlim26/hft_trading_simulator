numbers = [10,3,6,2,8,14]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
#print(max)

# To split up words in a sentence into a list
message = input(">")
words = message.split(' ')
print(words)