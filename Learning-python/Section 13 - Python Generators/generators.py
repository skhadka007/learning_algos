## Santosh Khadka
# Python Generators
'''
Generator functions 
    allows us to write a function that can send back a value 
    then later resume to pick up where it left off
        - useful in generating a sequence of values over time
        - uses 'yield' 
        - when used in code generator functions will automatically suspend and resume their execution and state
          around the last point of value generation - does not start and exit function for every yield.
    
    *Advantage: Instead of having to compute an entire series of values up front, the generator computes ONE value
                then waits util the next value is needed/called for. 
                - good way to save memory and time. Needed for very large lists. 
        - range() is also a generator - doesnt create the whole list at once
            - if list was needed would need to do, Ex: list(range(0, 20))
'''
def create_cubes_list(n):   # returns a list
    result = []
    for x in range(n):
        result.append(x**3)
    return result

def create_cubes_yield(n):  # yields integers after processing
    for x in range(n):
        yield x**3

def gen_fibonaci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b,a+b
        
def simple_gen(n):
    for x in range(n):
        yield x+10

def main():
    # for x in create_cubes_list(10):
        # print(x)
    
    # print(list(create_cubes_yield(10)))
    # c = create_cubes_yield(10)
    # print(type(c))  # <class 'generator'>   - doesnt print values
    
    # for x in create_cubes_yield(10):
    #     print(x)
    
    # for x in gen_fibonaci(10):
        # print(x)
    
    for num in simple_gen(5):
        print(num)
    print(simple_gen(5))     
        

if __name__ == "__main__":
    main()
