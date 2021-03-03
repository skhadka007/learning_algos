## Santosh Khadka
# Errors and Exceptions 

'''
Problem 1: 
Handle the exception thrown by the code below by using try and except blocks
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

'''
def prob1():
    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print("Error: Cannot use non-numeric values for arithmetic.")
    finally:
        print("Problem 1 - complete.")

'''
Problem 2
Handle the exception thrown by the code below by using try and except blocks. 
Then use a finally block to print 'All Done.'
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-6f985c4c80dd> in <module>()
      2 y = 0
      3 
----> 4 z = x/y
ZeroDivisionError: division by zero
'''
def prob2():
    try:     
        x = 5
        y = 0
        z = x/y
    except ZeroDivisionError:  
        print("Cannot divide by ZERO.")
    finally:
        print("All done - problem 2.")

'''
Problem 3
Write a function that asks for an integer and prints the square of it. 
Use a while loop with a try, except, else block to account for incorrect inputs.
---------------------------------------------------------------------------
Input an integer: null
An error occurred! Please try again!
Input an integer: 2
Thank you, your number squared is:  4
'''
def ask():
    while True:
        try:
            num1 = int(input("Input an integer: "))
        except:
            print("An error occured! Please try again!")
        else:
            print("Thank you, your number squared is: ", num1**2)
            break


def main():
    #prob1()
    #prob2()
    ask()

if __name__ == "__main__":
    main()