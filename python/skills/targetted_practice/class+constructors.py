class Person:
    def __init__(self,name):
        self.name = name            # Setting the name attribute of the object to the name argument passed 

    def talk(self):
        print(f'Hi, I am {self.name}')


john = Person("John Smith")
john.talk()

bob = Person("Bob Smitty")
bob.talk()