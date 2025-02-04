import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"{self.x}, {self.y}")

    def dist(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        
        
a = int(input())
b = int(input())
point1 = Point(a, b)
a1 = int(input())
b1 = int(input())
point2 = Point(a1, b1)
point1.show()
print(point1.dist(point2))
