# python program to generate random ints/strings/etc.
# Outputs to file
import random # random module

## PRINT TEST HERE
# prints random number between 0 and 9
# for x in range(0, 100): # prints 0 to 99 -> 100 elements
#     y = random.randint(0,9) # inclusive
#     print("Generation ", x, ": ", y)

manual_min = -1
manual_max = 123456789

int_min = 0
int_max = 100 
number_of_elements = 10000
total_elements = 0

## File write
fileName = "pre_sort.txt"
fileOpen = open(fileName, "w") # write only - overwritten 

## Integer generator
for x in range(0, number_of_elements - 1):
    num1 = random.randint(int_min, int_max) # inclusive
    fileOpen.write(str(num1) + "\n")
# Last line will be there to confirm how many elements there are. 
fileOpen.write(str(number_of_elements))

# MANUAL Input - manually insert smallest and largest values. 
#fileOpen.write(str(manual_min))
#fileOpen.write(str(manual_max))

## Float generator

## Char generator

## String generator

## Array generator 

## End
fileOpen.close()