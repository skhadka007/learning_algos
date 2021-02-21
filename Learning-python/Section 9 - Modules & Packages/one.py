## Santosh Khadka
# one.py

def func():
    print("Func() in one.py")


if __name__ == "__main__":
    # runs the code here if this file/program is being run directly - not called in another script
    print("one.py is being run directly!")
else:
    print("one.py has been imported!")