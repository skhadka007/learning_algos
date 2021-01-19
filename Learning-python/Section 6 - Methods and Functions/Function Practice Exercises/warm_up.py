## SANTOSH KHADKA
## Complete-Python-3-Bootcamp/03-Methods and Functions/03-Function Practice Exercises
## WARMUP SECTION:

def lesser_of_two_evens(a,b):
    '''
    LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd 
    '''
    if ((a%2 == 0) and (b%2 == 0)):
        if a < b:
            return a
        elif a > b:
            return b
        # return min(a, b)
    if ((a%2 != 0) or (b%2 != 0)):
        if a > b:
            return a
        elif b > a:
            return b
        # return max(a, b)

def animal_crackers(text):
    '''
    ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    '''
    text_1 = text.split()[0]
    text_2 = text.split()[1]
    if (text_1[0].capitalize() == text_2[0].capitalize()):
        return True
    else:
        return False
    # return text_1[0].capitalize() == text_2[0].capitalize()
    
def make_twenty(n1, n2):
    '''
    MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
    '''
    if (n1 == 20) or (n2 == 20):
        return True
    elif (n1 + n2 == 20):
        return True
    else:
        return False
    # return (n1+n2) == 20 or n1==20 or n2==20

def function_test(func_name):
    if "lesser_of_two_evens" in str(func_name):
        num = lesser_of_two_evens(2, 4)
        print(num)
        num = lesser_of_two_evens(2, 5)
        print(num)
    
    if "animal_crackers" in str(func_name):
        check = animal_crackers("Levelheaded Llama")
        print(check)
        check = animal_crackers("Crazy Kangaro")
        print(check)
    
    if "make_twenty" in str(func_name):
        print(make_twenty(20, 10)) #True
        print(make_twenty(12, 8)) #True
        print(make_twenty(2, 3))  #False
        

def main():
    #function_test("lesser_of_two_evens")
    #function_test("animal_crackers")
    function_test("make_twenty")
    
if __name__ == "__main__":
    main()