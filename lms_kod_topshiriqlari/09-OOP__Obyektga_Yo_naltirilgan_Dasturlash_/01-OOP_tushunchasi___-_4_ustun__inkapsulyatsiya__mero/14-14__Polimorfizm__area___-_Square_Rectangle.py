class Square:
    def __init__(self, s):
        self.s = s 
    def area(self):
        return self.s * self.s 
    
class Rectangle:
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def area(self):
        return self.w * self.h
parts = input().split()

if parts[0] == "kv":
    s = int(parts[1])
    shape = Square(s)
    print(shape.area())
elif parts[0] == "rect":
    w = int(parts[1])
    h = int(parts[2])
    shape = Rectangle(w, h)
    print(shape.area())