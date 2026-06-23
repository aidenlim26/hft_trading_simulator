# Inheritance is a mechanism for reusing code

# REPEATING CODE
class Dog:
    def walk(self):
        print("walk")

class Cat:
    def walk(self):
        print("walk")
         


# THIS IS HOW YOU PREVENT REDOING THE SAME CODE FOR DIFFERENT CLASSES
class Mammal:           # Kinda like the master class all inhertied classes has access to its code, but it can't access the inhertied class's specific functions etc.
    def walk(self):
        print("walk")
    
class Dog(Mammal):      # INHERITANCE
    pass                # pass is to say that nothing happens here + keep syntax correct

class Cat(Mammal):      # INHERITANCE
    def meow(self):     # You can still include code specific to the "Cat" class which only it can access
        print('Meow')

dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.meow()