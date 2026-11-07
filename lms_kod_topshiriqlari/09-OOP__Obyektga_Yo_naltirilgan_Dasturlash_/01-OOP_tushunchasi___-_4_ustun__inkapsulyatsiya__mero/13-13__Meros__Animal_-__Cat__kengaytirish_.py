class Animal:
    def __init__(self, name):
        self.name = name
        
class Cat(Animal):
    def sound(self):
        return f"{self.name}: Myau"
    
name = input()
cat = Cat(name)
print(cat.sound())