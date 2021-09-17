'''
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps, for every step it was noted if it was an uphill, , or a downhill, step. Hikes always start and end at sea level, and each step up or down represents a

unit change in altitude. We define the following terms:

    A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
    A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through. 

Example: 
8, UDDDUDUU
_/\      _
   \    /
    \/\/
    
'''

def countingValleys(steps, path):
    level = 0
    valley = False
    count = 0
    for x in path:
        if x == "U":
            level += 1
        elif x == "D":
            level -= 1
        if level < 0:
            valley = True
        if valley == True and level >= 0:
            valley = False
            count += 1
    print(count)
    
countingValleys(8, "UDDDUDUU")