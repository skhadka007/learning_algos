#!/bin/python3

import math
import os
import random
import re
import sys


class Car():
    def __init__(self, speed, units):
        self.speed = speed
        self.units = units
    def __str__(self):
        return str("Car with the maximum speed of " + str(self.speed) + " " + str(self.units))
        

class Boat:
    def __init__(self, speed):
        self.speed = speed
    def __str__(self):
        return str("Boat with the maximum speed of " + str(self.speed) + " knots")
    
def transformSentence(sentence):
    # Write your code here
    skip = 0
    print(sentence)
    new_sentence = ""
    
    for x in range(len(sentence)):
        if skip == 0:
            new_sentence += str(sentence[x])
            skip = 1
            continue
        if sentence[x] == " ":
            skip = 0
            new_sentence += str(sentence[x])
            continue
        
        if sentence[x].upper() < sentence[x-1].upper():
            new_sentence += str(sentence[x]).upper()
        elif sentence[x].upper() > sentence[x-1].upper():
            new_sentence += str(sentence[x]).lower()
        elif sentence[x].upper() == sentence[x-1].upper():
            new_sentence += str(sentence[x])
        
    print (new_sentence)
    return new_sentence

def main():
    if "c" < "b":
        print ("yes")
    else:
        print("no")
        
transformSentence("UDaxiHhEXDvxrCSnBacgHqTArgwuWRnHOSIZaYzfwnKIegYkdCmDlLTiZBxORdmCRjuTLSGWcBVHyJchDMioulfLLGViWVUCTUFR")
transformSentence("a Blue MOON")

# print("B" == "b")
# text = "upper"
# print(str(text).upper())

'''
UDaxiHhEXDvxrCSnBacgHqTArgwuWRnHOSIZaYzfwnKIegYkdCmDlLTiZBxORdmCRjuTLSGWcBVHyJchDMioulfLLGViWVUCTUFR
UDAxIHhExDvxRCsNBAcghqtArGwUwRNHosIzAyzFwNKIEgyKDCmDlLtIzBxOrDmCrJuTLsGwCBvHyJChDmIouLFlLGvIwVUCtuFr
'''