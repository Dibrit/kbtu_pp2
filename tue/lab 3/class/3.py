class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, a, b):
        self.length = a
        self.width = b

    def area(self):
        return self.length * self.width


a = Shape()
print("Shape area:", a.area())
m = int(input())
s = Square(m)
print("Square area:", s.area())
m1 = int(input())
m2 = int(input())
c = Rectangle(m1, m2)
print("Rectangle area:", c.area())
