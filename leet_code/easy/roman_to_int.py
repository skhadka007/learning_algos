## Santosh Khadka
# https://leetcode.com/problems/roman-to-integer/
'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "IV"
Output: 4

Example 3:
Input: s = "IX"
Output: 9

Example 4:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
#class Solution(object):
def intToRoman(num):
    """
    :type s: str
    :rtype: int
    """
    if s>0 and s<5:     # I - 1
        print("0-4")
    if s>=5 and s<10:   # V - 5
        print("5-9")
    if s>=10 and s<50:  # X - 10
        print("10-49")
    if s>=50 and s<100: # L - 50
        print("50-99")
    if s>=100 and s<500:    # C - 100
        print("100-499")
    if s>=500 and s<999:    # D - 500
        print("500-999")
    if s>=1000 and s<=3999: # M - 1000
        print("1000-3999")
    else:
        print("ERROR - Out of range: [1, 3999]")

def romanToInt_v1(s):   # WORKS #################################
    """
    :type s: str
    :rtype: int
    
    Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
    """
    s = s+"A"
    n = 0
    value = 0
    for x in s:
        # print(s[n])
        if s[n] == "A":
            return value
        if 'M' in s[n]:     # 1000s
            value += 1000
        elif 'D' in s[n]:   # 500s
            value += 500
        elif 'C' in s[n] and 'D' in s[n+1]: # 400
            value += 400
            n += 1
        elif 'C' in s[n] and 'M' in s[n+1]: # 900
            value += 900
            n += 1
        elif 'C' in s[n]:   # 100s
            value += 100
        elif 'L' in s[n]:   # 50s
            value += 50
        elif 'X' in s[n] and 'L' in s[n+1]: # 40
            value += 40
            n += 1
        elif 'X' in s[n] and 'C' in s[n+1]: # 90
            value += 90
            n += 1
        elif 'X' in s[n]:   # 10s
            value += 10
        elif 'V' in s[n]:   # 5s
            value += 5
        elif 'I' in s[n] and 'V' in s[n+1]: # 4
            value += 4
            n += 1
        elif 'I' in s[n] and 'X' in s[n+1]: # 9
            value += 9
            n += 1
        elif 'I' in s[n]:   # 1
            value += 1
        else:
            print("ERROR: INVALID INPUT")
        n += 1
    return value

print(romanToInt_v1("III"))        # 3
print("=======================")
print(romanToInt_v1("IV"))         # 4
print("=======================")
print(romanToInt_v1("IX"))         # 9
print("=======================")
print(romanToInt_v1("LVIII"))      # 58
print("=======================")
print(romanToInt_v1("MCMXCIV"))    # 1994

def romanToInt_v2(s):
    # dictionary
    romans = {'I':1, 'IV':4, 'IX':9, 'V':5, 'X':10, 'XL':40, 'XC':90, 'L':50, 'C':100, 'CD':400, 'CM':900, 'D':500, 'M':1000}

def romanToInt_v3(s):
    for x in s:
        if ('IV' in s) or ('IX' in s) or ('XL' in s) or ('XC' in s) or ('CM' ):
            pass

# romanToInt("III")
# romanToInt("IV")
# romanToInt("IX")
# romanToInt("LVIII")
# romanToInt("MCMXCIV")