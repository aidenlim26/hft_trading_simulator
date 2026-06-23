class PointTest:                # When naming classes, there shall be no underscores, each word starts with a capital letter
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 = PointTest()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = PointTest()
point2.x = 1
print(point2.x)