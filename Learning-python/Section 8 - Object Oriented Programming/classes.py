'''
CLASS BLUEPRINT

class NameofClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def some_method(self):
        #perform some action
        print(self.param1)
'''

'''
mylist = [5, 2, 3, 1]  # mylist is an object - everthing in python is an object
mylist.sort()          # .sort() is a function for the mylist object. Object type is list.
print(mylist)

By using classes we are created user defined objects - custom objects.
Instance - specific object created from a class.
'''

class Dog:
    
    species = 'mammal'
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        
    def bark(self, dog_id): # new methods always need the 'self' keyword/parameter
        print("WOOF! My name is:", self.name, "and my ID is:", dog_id)   # Prints its own name - self.name -> Is able to reference itself. 
        
mydog = Dog('Shitzu', 'Spot') 
mydog2 = Dog("Collie", 'Hunter')

# print(mydog.species)
# print(mydog2.breed)
# mydog.bark(3214)

class Circle():
    # Class object attribute
    pi = 3.14
    
    def __init__(self, radius=1):   # 'radius=1' default parameter if nothing is sent through
        self.radius = radius
        self.area = radius*radius*Circle.pi # or self.pi
    def get_circum(self):
        return self.radius*self.pi*2

my_circle = Circle()
print("Pi:", my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circum())
my_circle = Circle(30)
print("rad", my_circle.radius)
print("circ", my_circle.get_circum())
print("area", my_circle.area) # If I change the radius after inital creation then it wont change the area - will use the same radius it started with