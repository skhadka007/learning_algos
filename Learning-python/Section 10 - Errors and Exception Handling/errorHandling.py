## Santosh Khadka
'''
~3 Keywords
try: block of code to be attempted
except: will execute IF error in try block
finally: will execute REGARDLESS of error. Always executed.
'''

from typing import final


def add(n1, n2):
    print(n1+n2)
    
try:
    # WANT TO ATTEMPT, but may create error
    #result = 10 + "10" # error
    result = 10 + 10 # no error
except:
    # IF ERROR, this will happen
    print("Issue: Did not add correctly")
else:
    print("Addition happened correctly!")
    print(result)
finally:
    print("Attempt over.")