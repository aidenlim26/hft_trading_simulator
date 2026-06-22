customer = {
    "name" : "John Smith",
    "age" : 30,
    "is_verified" : True
}

#print(customer["name"])     # Use square brackets to call the dictionary key to get the value
                             # However, if there isnt a key matching your "name", the program will crash

# Therefore, use .get
print(customer.get("birthdate"))    # Because if theres no key matching, the program will output "None"
print(customer.get("birthdate", "Jan 1 1980")) # But you can also put in a default value for no key matches



