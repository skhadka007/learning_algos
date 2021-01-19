## SANTOSH KHADKA
## Complete-Python-3-Bootcamp/03-Methods and Functions/03-Function Practice Exercises
## Level 1 Problems:

def old_macdonald(name):
    '''
    OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
    '''
    new_name = ""
    for x in range(len(name)):
        if x == 0 or x == 3:
            new_name += name[x].capitalize()
        else:
            new_name += name[x]
    return new_name

def master_yoda(text):
    '''
    MASTER YODA: Given a sentence, return a sentence with the words reversed
    '''
    new_text = ""
    temp = text.split()
    
    for x in range(len(temp)):
        if x == 0:
            new_text += temp[len(temp)-1-x].capitalize()
            new_text += " "
        else:
            if str(temp[len(temp)-1-x]) == "i" or str(temp[len(temp)-1-x]) == "I":
                new_text += temp[len(temp)-1-x].capitalize()    
            else:
                new_text += temp[len(temp)-1-x].lower()
            new_text += " "
    new_text.strip()
    return new_text

def almost_there(n):
    '''
    ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
    '''
    if(abs(100-n) < 11) or (abs(200-n) < 11):
        return True
    else:
        return False

def function_test(func_name):
    if "old_macdonald" in str(func_name):
        print(old_macdonald("macdonald"))

    if "master_yoda" in str(func_name):
        print(master_yoda("I am home"))
        print(master_yoda("We are ready"))
    
    if "almost_there" in str(func_name):
        print(almost_there(90))
        print(almost_there(104))
        print(almost_there(150))
        print(almost_there(209))
        
def main():
    #print("Function test: old_macdonald "); function_test("old_macdonald")
    #function_test("master_yoda")
    #function_test("almost_there")
    pass
if __name__ == "__main__":
    main()