class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name}: Vov!"
    
name = input()
dog = Dog(name)
print(dog.bark())