## Santosh Khadka
'''
~Object Oriented Programming Challenge~
For this challenge, create a bank account class that has two attributes:
    owner
    balance
and two methods:
    deposit
    withdraw
- As an added requirement, withdrawals may not exceed the available balance.
- Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''

class Account:
    def __init__(self, name, ammount=0):    # Should start with a default of 0
        self.name = name
        self.ammount = ammount
    
    def __str__(self):
        # print("Account owner    :", self.name)
        # print("Account balance  :", self.ammount)
        print1 = "Account owner    : " + self.name + '\n' + "Account balance  : $" + str(self.ammount)
        return (print1)
    
    def owner(self):
        print(self.name)
    
    def balance(self):
        print(self.ammount)
    
    def deposit(self, deposit):
        self.ammount += deposit
        print("Deposit Accepted")
    
    def withdraw(self, withdraw):
        if (self.ammount - withdraw < 0):
            print("Funds Unavailable!")
        else:
            self.ammount -= withdraw
            print("Withdrawal Accepted")
    

# 1. Instantiate the class
acct1 = Account('Jose',100)
# 2. Print the object
print(acct1)
# 3. Show the account owner attribute
acct1.owner()
# 4. Show the account balance attribute
acct1.balance()
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

#print(acct1)