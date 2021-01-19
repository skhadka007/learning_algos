## USE: map(function, *iterable)
'''
- Map: is basically a shorter for-loop. Says take every item in my list/etc. and apply it to that function.. similar to a for-loop iterating through that list/etc. 
    Note: Dont need to add the '()' after function name

- Filter: Similar to map

- Lambda: 'lambda parameter_list: expression, [list/iterable]'
    Anonymous function, something you would only use once. ex) def square(num): return num**2 --> lambda num: num**2 --> print(list(map(lambda num:num**2, mynums)))
        When you want to use a 'function' but it's something really basic that you don't need to create a whole function/method. 
        BUT, is limited to just that line of code aka not readily repeatable but useful with map and filter built in functions.
'''
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
    
def check_even(num):
    return num%2 == 0

def square(num):
    return num**2
    
def main():
    names = ["Andy", "Eve", "Sally"]
    nums = [1,2,3,4,5,6,7,8]
    for item in map(splicer, names):
        print(item)
    print(list(map(splicer, names)))
    
    print(list(filter(check_even, nums)))
    
    ## Lambda equivalents 
    print(list(map(lambda num:num**2, nums)))
    print(list(filter(lambda num:num%2 == 0, nums)))
    
if __name__ == "__main__":
    main()