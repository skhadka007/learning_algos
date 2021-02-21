## Santosh Khadka
# two.py
import one

def func():
    print("Func() in two.py")

one.func()

if __name__ == "__main__":
    # runs the code here if this file/program is being run directly - not called in another script
    print("two.py is being run directly!")
else:
    print("two.py has been imported!")