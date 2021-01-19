## Santosh Khadka - 03-Methods and Functions/08-Functions and Methods Homework.ipynb
import re
import string

def vol(rad):
    '''
    Write a function that computes the volume of a sphere given its radius. 
        Volume=(4/3)*pi*(radius^3) 
    '''
    c1 = 4/3
    pi = 3.14
    volume = c1*pi*(rad**3)
    return volume

def ran_check(num, low, high):
    '''
    Write a function that checks whether a number is in a given range (inclusive of high and low)
    '''
    if(num <= high) and (num >= low):
        print(num, 'is in the range between', low, 'and', high)
    #return (num in range(low, high+1))
        
def ran_bool(num, low, high):
    '''
    Write a function that checks whether a number is in a given range (inclusive of high and low)
    '''
    return ((num <= high) and (num >= low))

def up_low(s):
    '''
    Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
    '''
    uppers = 0; lowers = 0
    regex = re.compile('[^a-zA-Z]') # removes all non-alphabet characters from the string
    string1 = regex.sub('', s)
    #print(string1)
    for char in string1:
        if char == char.lower():
            lowers += 1
        else:
            uppers += 1
    print('Original String :', s)
    print('No. of Upper case characters :', uppers)
    print('No. of Lower case Characters :', lowers)
 
def unique_list(lst):
    '''
    Write a Python function that takes a list and returns a new list with unique elements of the first list.
    '''
    u_set = set()
    u_list = [] 
    for x in range(len(lst)):
        #print(lst[x])
        u_set.add(lst[x])
    u_list += u_set # can also do "u_list.extend(u_set)"
    return u_list
    #return list(set(lst)) # 1 line solution: turns given list into set(removes duplicates) then turns set into list

def multiply(numbers):
    '''
    Write a Python function to multiply all the numbers in a list.
    '''
    total = numbers[0]
    for x in range(1, len(numbers)):
        total = total*numbers[x] 
    return total

def palindrome(s):
    '''
    Write a Python function that checks whether a word or phrase is palindrome or not.
    '''
    s = s.replace(' ', '')
    reverse_s = s[::-1]
    return s == reverse_s
    #return s == s[::-1]

def isPangram(str1, alphabet=string.ascii_lowercase): # alphabet set by default so no alphabet argument needed
    # alphabet = abcdefghijklmnopqrstuvwxyz
    '''
    Write a Python function to check whether a string is pangram or not. 
    (Assume the string passed in does not have any punctuation)
        *Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
            For example : "The quick brown fox jumps over the lazy dog"
    '''
    for x in range(len(alphabet)):
        if alphabet[x] in str1:
            continue
        else:
            return False
    return True
    

def func_check(func_name):
    if "vol" in str(func_name):
        print('{0:.6g}'.format(vol(2))) # formatted output 

    if "ran_check" in str(func_name):
        ran_check(5, 2, 7)
    
    if "ran_bool" in str(func_name):
        print(ran_bool(3, 1, 10))
    
    if "up_low" in str(func_name):
        up_low("Hello Mr. Rogers, how are you this fine Tuesday?")

    if "unique_list" in str(func_name):
        print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
    
    if "multiply" in str(func_name):
        print(multiply([1,2,3,-4]))
    
    if "palindrome" in str(func_name):
        print(palindrome("helleh"))
        print(palindrome("tenet tenet"))
        print(palindrome("asdasd"))
    
    if "isPangram" in str(func_name):
        #alphabet = 'abcdefghijklmnopqrstuvwxyz'
        #print(isPangram("The quick brown fox jumps over the lazy dog", alphabet))
        print(isPangram("The quick brown fox jumps over the lazy dog"))
        print(isPangram("This should return False"))
    
def main():
    # func_check(vol)
    # func_check(ran_check)
    # func_check(ran_bool)
    # func_check(up_low)
    # func_check(unique_list)
    # func_check(multiply)
    # func_check(palindrome)    
    func_check(isPangram)

if __name__ == "__main__":
    main()