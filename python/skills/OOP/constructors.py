class Point:
    def __init__(self,x,y):         # __init__ is short for "initialise"
        self.x = x
        self.y = y

    def move(self):
        print('move')
    def draw(self):
        print('draw')
    
# A constructor is a function that gets called at the time of creating an object

point = Point(10,20)        # Uses the init function to assing (10,20)
print(point.x)