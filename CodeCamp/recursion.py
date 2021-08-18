'''
SANTOSH KHADKA

We have defined a function called countdown with one parameter (n). 
The function should use recursion to return an array containing the 
integers n through 1 based on the n parameter. If the function is 
called with a number less than 1, the function should return an empty array. 
For example, calling this function with n = 5 should return the array [5, 4, 3, 2, 1]. 
Your function must use recursion by calling itself and must not use loops of any kind.
'''

def countdown(n):
    if (n < 1):
        return []
    else:
        countArray = countdown(n - 1)
        countArray.insert(0, n)
        return countArray
    
    return

print(countdown(5))

def countdown2(n):
    if (n < 1):
        return []
    else:
        num = countdown2(n-1)
        pass

print(countdown(5))