# Santosh Khadka
'''
Iterators and Generators Homework

You would want to use a generator with a yield statement when there is/could be a space issue from the output and you don't want to save a lot of data in memory.
Also when you don't need all the data at once, just one at a time. 
'''
import random

def gensquares(N):
    # Generator that generates the squares of numbers up to some number N.
    for nums in range(N):
        yield (nums**2)

def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)

def toIter(text):   # change variable into iter type
    s_iter = iter(text)
    for x in range(len(text)):
        print(next(s_iter))

def genComp(givenList): # Generator Comprehension:
    my_list = givenList
    
    gencomp = (item for item in my_list if item > 3)
    for item in gencomp:
        print(item)
        
def test(case):
    if case == 1:
        for x in gensquares(10):
            print(x)
    if case == 2:
        for num in rand_num(1, 10, 12):
            print(num)
    if case == 3:
        toIter("hello")
    
    if case == 4:
        genComp([1,2,3,4,5])


    
test(1)