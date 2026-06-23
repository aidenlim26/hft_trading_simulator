import random


print(random.random())         # Generates value between 0 and 1
print(random.randint(10,20))   # Generates value between 10 and 20

members = ['John','Mary','Bob','Bosh']
leader = random.choice(members)         # Picks a random index from the list
print(leader)