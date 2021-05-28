# Santosh Khadka
# Section 12 - Decorators

'''
Tack on extra functionality to an already existing function. Placed on top of the original function.

Useful when: Append to an existing function while still retaining the ability to use the original, pre-change, function. On/off.
'''

def func1():
    x = 2
    return x

def main():
    print(func1())
    
if __name__ == "__main__":
    main()