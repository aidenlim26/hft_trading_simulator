phone = str(input("Phone: "))

phonenumber = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

output = ""
for i in phone:
    output += phonenumber.get(i, "!") + " "
print(output)