## SANTOSH KHADKA
## Complete-Python-3-Bootcamp/03-Methods and Functions/03-Function Practice Exercises
## Level 2 Problems:

def has_33(nums):
    '''
    FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    '''
    previous = nums[0]
    for x in range(1, len(nums)):
        if x == 1:
            if (previous == 3) and (nums[1] == 3):
                return True
        else:
            if nums[x-1] == 3 and nums[x] == 3:
                return True
    return False 
            
def paper_doll(text):
    '''
    PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    '''
    new_text = ""
    for x in range(len(text)):
        new_text += text[x]
        new_text += text[x]
        new_text += text[x]
        # new_text += text[x]+text[x]+text[x]
    return new_text

def blackjack(a, b, c):
    '''
    BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
    Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    '''
    total = a + b + c
    if total <= 21:
        return total
    elif (total > 21) and (a==11 or b==11 or c==11):
        if (total - 10) > 21:
            return "BUST" 
        else:
            return total - 10    
    else:
        return "BUST"

def summer_69(arr):
    '''
    SUMMER OF '69: Return the sum of the numbers in the array, 
    except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
    Return 0 for no numbers.
    '''
    total = 0
    ignore = 0
    if (len(arr) == 0):
        return 0
    for x in range(len(arr)):
        if arr[x] == 6:
            ignore = 1
        if ignore == 0:
            total += arr[x]
        if arr[x] == 9:
            ignore = 0
    return total
    
def function_test(func_name):
    if "has_33" in str(func_name):
        print(has_33([1, 3, 3]))
        print(has_33([1, 3, 1, 3]))
        print(has_33([3, 1, 3]))
    
    if "paper_doll" in str(func_name):
        print(paper_doll("Hello"))
        print(paper_doll("Mississippi"))
        
    if "blackjack" in str(func_name):
        print(blackjack(5,6,7))  #--> 18
        print(blackjack(9,9,9))  #--> 'BUST'
        print(blackjack(9,9,11)) #--> 19

    if "summer_69" in str(func_name):
        print(summer_69([1, 3, 5]))          #--> 9
        print(summer_69([4, 5, 6, 7, 8, 9])) #--> 9
        print(summer_69([2, 1, 6, 9, 11]))   #--> 14
        print(summer_69([]))                 # EMPTY --> 0
        
def main():
    #function_test("has_33")
    #function_test("paper_doll")
    #function_test("blackjack")
    function_test("summer_69")

if __name__ == "__main__":
    main()