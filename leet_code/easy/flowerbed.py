## Santosh Khadka
# https://leetcode.com/problems/can-place-flowers/
'''
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return if n new flowers can be planted in the flowerbed without 
violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''
# class Solution(object):
def canPlaceFlowers_v1(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    flowers = n
    can_place = False
    n = 0
    count = 0
    if len(flowerbed) > 3:
        for x in flowerbed:
            print(x)
            if n >= len(flowerbed)-1:
                break
            if flowerbed[n] == 1:
                if flowerbed[n+1] == 0 and flowerbed[n+2] == 0 and flowerbed[n+3] == 0:
                    count += 1
                    n += 2
            elif flowerbed[n] == 0:
                if flowerbed[n+1] == 0:
                    count += 1
                    n += 2
    if count >= flowers:
        can_place = True
    else:
        can_place = False
    return can_place

def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    green = 0
    index = 1
    count = 0

    if len(flowerbed) > 2:
        for x in flowerbed[1:]:
            if flowerbed[index] == 1:
                # [0, 1, 0, 1, 1, 0, 1]
                if (flowerbed[index-1] == 0) and (flowerbed[index+1] == 0):
                    count += 1
                
    else:
        pass

flowerbed1 = [1,0,0,0,1]
print(canPlaceFlowers(flowerbed1, 1))
print(canPlaceFlowers(flowerbed1, 2))