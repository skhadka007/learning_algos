## Santosh Khadka
# https://leetcode.com/problems/palindrome-number/
'''
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false

Follow up: Could you solve it without converting the integer to a string?
'''

# class Solution(object):
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    
    string_x = str(x)[::-1]
    if string_x == str(x):
        return True
    else:
        return False

print(isPalindrome(121))    # true
print(isPalindrome(-121))   # false
print(isPalindrome(10))     # false
print(isPalindrome(-101))   # false