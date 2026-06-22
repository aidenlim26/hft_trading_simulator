def square(number):
    return number * number

result = square(3)
#print(result)

# Example function
def emoji_converter(message):
    words = message.split(' ')

    emoji = {
        ":)" : "😁",
        ":(" : "🙁",
        ":P" : "😛"
    }

    output = ""
    for i in words:
        output += emoji.get(i, i) + ' '
    return output

message = str(input("Enter: "))
print(emoji_converter(message))
