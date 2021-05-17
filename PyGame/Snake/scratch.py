# Santosh Khadka

from collections import namedtuple
from typing import AsyncIterable
from pygame.constants import SCRAP_SELECTION

from pygame.locals import Color


class Car:
    def __init__(self, wheels, ai, color):
        self.wheels = wheels
        self.ai = ai
        self.color = color
    
    def run(self):
        print(self.wheels, self.ai, self.color)

toyota = Car(4, "no", "blue")
toyota.run()


class Employee:
    def __init__(self, name, title, yearly_pay, total_months, promotion):
        self.name = name
        self.title = title
        self.yearly_pay = yearly_pay
        self.total_months = total_months
        self.promotion = promotion
    
    def name_title(self):
        print("Employee: ", self.name,", Title: ", self.title)
    
    def promote(self):
        print("Employee: ", self.name,", Promotable: ", self.promotion)

Steve = Employee("Steve Rogers", "Captain", 50000, 6, "NO")        
Steve.name_title()
Steve.promote()