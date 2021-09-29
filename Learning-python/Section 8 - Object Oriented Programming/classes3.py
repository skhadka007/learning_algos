class Person:
    def __init__(self,initialAge):
        self.age = 0
        self.initialAge = initialAge
        # Add some more code to run some checks on initialAge
        if self.initialAge > 0:
            self.age = self.initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
        
def test(case):
    if case == 1:
        Person(4).amIOld()
        Person(-1).amIOld()
        Person(10).amIOld()
        Person(16).amIOld()
        Person(18).amIOld()
        
        
        
test(1)