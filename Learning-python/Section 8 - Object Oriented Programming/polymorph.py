class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"
    
Budd = Dog("Budd")
print(Budd.speak())

print(type(Budd))
print(type(Budd.speak()))

class Animal():
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this abstract method")   # subclass HAS to make this method


class Cat(Animal):
    def speak(self):
        return self.name + " says MEOW!"    # Inherits self.name from Animal

Tom = Cat("Tom")
print(Tom.speak())