## Santosh Khadka

class Animal():
    
    def __init__(self):
        print("Animal created")
    
    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")
        

class Dog(Animal):  # inherits from the Animal(base class) class. Dog derives from Animal class
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    
    def who_am_i(self):
        print("I am a dog!")
        
Budd = Dog()

Budd.eat()  # inherits from Animal class even though dog doesnt have eat() method
Budd.who_am_i() # Base class method overwritten 