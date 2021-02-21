import math
from typing import Counter

## Problem 1:
class Line:
# Fill in the Line class methods to accept coordinates as a pair of tuples 
# and return the slope and distance of the line.

    def __init__(self,coor1,coor2):
        self.coor1 = coor1 
        self.coor2 = coor2
    
    def distance(self):
        distance = ((self.coor2[0]-self.coor1[0])**2)+((self.coor2[1]-self.coor1[1])**2)
        return math.sqrt(distance)
    
    def slope(self):
        slope = (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
        return slope

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print("Distance     :", li.distance())
print("Slope        :", li.slope())

## Problem 2: Fill in the class
class Cylinder:    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        volume = 3.14*(self.radius**2)*self.height
        return volume
    
    def surface_area(self):
        surface_area = (2*3.14*self.radius*self.height)+(2*3.14*self.radius**2)
        return surface_area

cyl1 = Cylinder(2, 3)
print("Volume       :", cyl1.volume())
print("Surface Area :", cyl1.surface_area())

