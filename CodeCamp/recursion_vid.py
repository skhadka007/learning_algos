'''
https://www.youtube.com/watch?v=IJDJ0kBx2LM
SANTOSH KHADKA
'''

'''
~~~~~~~~~NOTES~~~~~~~~~
- Recursion function/method has a call stack. Could result in stack overflow. 
    - Thats why base case is needed, so it stops eventually - eventually returns a value. 

'''
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# String reversal - recursive method
#def reverseString(inputString):
    # What is the base case - when can I no longer continue?
        # What is the smallest input I could put in to immediately return a value? > empty string 
    # What is the smallest amount of work I can do in each iteration?
    
# def reverseString(inputString): # hello
#     if (inputString == ""):
#         return ""
#     else:
#         return reverseString(inputString[1:]) + inputString[0]

# print(reverseString("hello")) 
# print(reverseString("reverse"))
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# def palindrome(inString): # kayak
#     if (inString == "" or len(inString) == 1):
#         return True
#     else:
#         if inString[0] == inString[-1]: 
#             return palindrome(inString[1:-1])       
#     return False

# print(palindrome("kayak"))
# print(palindrome("racecar"))
# print(palindrome("santosh"))
# print(palindrome("k"))
# print(palindrome(""))
# print(palindrome("kayaka"))
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# Decimal to Binary - 
# def decToBinary(num, result = ""):
#     if (num == 0):
#         return result;
#     else:
#         result = str(num%2) + result
#         return decToBinary(num//2, result)
    
# print(decToBinary(233)) # 11101001
# print(decToBinary(22)) # 10110
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# Factorial

# def getFactorial(num):
#     if (num == 0) or (num == 1):
#         return 1
#     else:
#         return num*getFactorial(num - 1)
        
# print(getFactorial(5)) # 120
# print(getFactorial(8)) # 40320
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# Sum of Natural Numbers


#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````

