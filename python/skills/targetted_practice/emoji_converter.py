message = str(input("Enter: "))

words = message.split(' ')

emoji_converter = {
    ":)" : "😁",
    ":(" : "🙁",
    ":P" : "😛"
}

output = ""
for i in words:
    output += emoji_converter.get(i, i) + ' '

print(output)