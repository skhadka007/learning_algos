# Santosh Khadka
import math

# help(math)    # Shows help data. What it supports etc.

value = 4.55

# print(math.floor(value))        # always removes the decimal place. Always rounds down.
# print(math.ceil(value))         # always rounds up. Opposite of floor()
# print(round(4.5))               # Output: 4: X.5 will always round down when even 
# print(round(5.5))               # Output: 6: X.5 will always round up when odd     - Done to get ride of a large ammount of over rounding to just top/bottom. 

# print(math.pi)  # 3.141592653589793
# from math import pi     # dont need to use 'math'.pi
# print(pi)       # 3.141592653589793

# print(math.e)
# print(math.inf)     # infiniti      "inf"
# print(math.nan)     # Not a Number  "nan"

'''
Numpy library used for heavy math usuage. Ifficient and deeper than just the math module
'''

# print(math.log(math.e))
# print(math.log(100, 10))        # value, base. So what number(x) is: 100 = 10^x     x = 2 -> 10^2 = 100

# print(math.sin(10))         # output is in radians
# print(math.degrees(math.pi/2))
# print(math.radians(180))

import random

# print(random.randint(0, 100))   # inclusive
random.seed(101)                # what random seed to use - so although 'random' will give the same numbers within that seed. 

## Random list
myRandList = list(range(0,20)) # non randomized list
print(myRandList)
# print(random.choice(myRandList))    # get random value from myRandList
# SAMPLE with replacement - can pick the same number more than once
# print(random.choices(population=myRandList, k=10))  # [16, 18, 10, 7, 0, 10, 12, 18, 9, 15]  - k = # of values
# SAMPLE without replacement - cannot pick the same number twice
# print(random.sample(population=myRandList, k=10))
# SHUFFLE list
# random.shuffle(myRandList)  # done in place
# print(myRandList)

#  Distributions
uniformDistrib = random.uniform(a=0, b=100)
gauss1 = random.gauss(mu=0, sigma=1)

## Can do more with numpy