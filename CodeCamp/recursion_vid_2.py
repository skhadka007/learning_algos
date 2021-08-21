'''
https://www.youtube.com/watch?v=IJDJ0kBx2LM
SANTOSH KHADKA
'''

'''
~~~~~~~~~NOTES~~~~~~~~~
- Recursion function/method has a call stack. Could result in stack overflow. 
    - Thats why base case is needed, so it stops eventually - eventually returns a value. 

'''

#```````````````````````````````````````````````````````````````````````````````````````
# Sum of Natural Numbers
# Take a number and add the individual elements together.
# EX) 5: 1+2+3+4+5 = 15

# def sumOfNaturalNumbers(num):
#     if (num <= 1):
#         return num
#     else:
#         return sumOfNaturalNumbers(num-1) + num

# print(sumOfNaturalNumbers(0)) # 0 
# print(sumOfNaturalNumbers(1)) # 1
# print(sumOfNaturalNumbers(5)) # 15
# print(sumOfNaturalNumbers(10)) # 55
# print(sumOfNaturalNumbers(55)) # 55
#```````````````````````````````````````````````````````````````````````````````````````

#```````````````````````````````````````````````````````````````````````````````````````
'''
Divide & Conquer - Use of Recursion
1) Divide a problem into several smaller subproblems.
    Normally, the subproblems are similar to the original.
2) Conquer the subproblems by solving them recursivley.
    Base case: solve small enough problems by brute force.
3) Combine the solutions to get a solution to the subproblems.
    And finally a solution to the original problem.
4) Divide and Conquer algorithms are normally recursive.
'''
# Binary search
# searchArray = [-4, -2, 0, 1, 2, 5, 6, 7, 8, 9, 11, 20, 21]

# def binarySearch(searchArray, left, right, x): # (array itself, leftMost index aka 0, rightMost index, value we're looking for)
#     if(left > right):  # Base error check - range error
#         print("Index Range Error - Array might be unsorted.")
#         return -1
    
#     mid = (left + right) // 2   # Base case check & getting mid value

#     if (x == searchArray[mid]):
#         return mid

#     if (x < searchArray[mid]):  # If find value is less than the mid value (left split)
#         return binarySearch(searchArray, left, mid-1, x)

#     return binarySearch(searchArray, mid+1, right, x) # Case when find value is higher than mid value (right split)

# # print(binarySearch(searchArray, 0, len(searchArray)-1, -4))
# # print(binarySearch(searchArray, 0, len(searchArray)-1, 11))
# # print(binarySearch(searchArray, 0, len(searchArray)-1, 0))

#```````````````````````````````````````````````````````````````````````````````````````

#```````````````````````````````````````````````````````````````````````````````````````
# Fibonacci (Non-Optimized)
# F(n) = F (n-1) + F (n-2); F(0) = 0 F(1) = 1

# def fibonacci(num):
#     if (num == 1 or num == 0):
#         return num
#     else:
#         return fibonacci(num-1) + fibonacci(num-2) # according to the formula

# print(fibonacci(1))     # 1
# print(fibonacci(4))     # 3
# print(fibonacci(8))     # 21
# print(fibonacci(12))    #144

#```````````````````````````````````````````````````````````````````````````````````````

#```````````````````````````````````````````````````````````````````````````````````````
# Merge Sort

from _typeshed import Self, StrPath


mergeSortArray = [-12, -122, -5, -1, 0 , 1, 2, 5, 7 , 9, 23]

class MergeSort():
    def __init__(self, data):
        self.data = data
        self.start = 0
        self.end = len(data)-1



#```````````````````````````````````````````````````````````````````````````````````````