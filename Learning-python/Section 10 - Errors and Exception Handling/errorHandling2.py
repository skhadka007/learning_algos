## Santosh Khadka
'''
built in exceptions: https://docs.python.org/3/library/exceptions.html
'''
def input_test():
    try:
        #f = open('testfile.txt', 'w')  # No error
        f = open('testfile.txt', 'r')   # Causes OS Error
        f.write("Write a test line")
    except TypeError:
        print("There was a type error!")
    except OSError:
        print("There was an OS Error!")
    except: # All other exceptions
        print("Other error!")
    finally:
        print("Attempt over.")


def ask_for_int():
    print("====================")
    while True:
        try:
            number = int(input("Enter a number: "))
        except:
            print("That was not a number!")
        else:
            print("Correct input!")
            break       # will break loop once correct input is entered
        finally:
            print("End of this attempt!")
            print("====================")
            
#input_test()
ask_for_int()