## Santosh Khadka
# https://leetcode.com/problems/two-sum/
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
'''

#class Solution(object):
    
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    output = []
    loc_x = 0
    loc_y = 1
    n = 1
    for x in nums:
        for y in nums[n:]:
            # print(x, y, ":", x+y)
            # print(loc_x)
            # print(loc_y)
            if x + y == target:
                output.append(loc_x)
                output.append(loc_y)
                return output
            loc_y += 1
        n += 1
        loc_y = n
        loc_x += 1

# nums1 = [2, 7, 11, 15]
# target1 = 9
nums1 = [3, 2, 4]
target1 = 6

nums2 = [3,2,3]
target2 = 6

nums3 = [3,3]
target3 = 6

print(twoSum(nums1, target1), '\n')
print(twoSum(nums2, target2), '\n')
print(twoSum(nums3, target3), '\n')