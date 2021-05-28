# Santosh Khadka
# Section 12 - Python Decorators

def func1():
    # print("hello")
    return "hello"

def hello(name="Santosh"):
    '''
    Because greet() is limited in scope to only hello() 
    you can have hello() return the function greet()/etc. to increase scope
    '''
    print("function hello() has been executed")

    def greet():    # scope is limited to this hello function, can only execute inside hello
        return "\tfunction greet() inside function hello()" # \t is TAB
    
    def welcome():
        return "\tfunction welcome() inside function hello()"

    # print(greet())  # can only execute inside hello()
    # print(welcome())

    if name == "Santosh":
        return greet    # will only return the function if 'greet' and not 'greet()'
                        # because 'greet' is returning function location/address
    else:
        return welcome

def test1():
    return "Santosh"

def more(some_function):
    print("Other code here...")
    print(some_function())  # Returning a function

def new_decorator(a_function):
    def wrap_func(): # new functionality that you want the passed in function to have
        print("code before the original function - proof of concept")
        a_function()
        print("code after the original function")
    return wrap_func

def main():
    func1()
    # print(func1)
    x = func1()
    # print(x)

    hello2 = func1   # if func1 is changed after this then hello will still return "hello"
    # print(hello2())  
    # hello()
    # print(hello())
    # new_func = hello()
    # new_func()
    # print(new_func())
    more(test1) # will not work with 'test()' - want to pass in the FUNCTION not the STRING

if __name__ == '__main__':
    main()