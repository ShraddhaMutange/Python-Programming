"""
---------------------------------------------------------------------------------------------------------------------
Problem :   Write a Python program to implement a class named BankAccount with the following specifications:
            - The class should contain two instance variables:
                - Name (Account holder name)
                - Amount (Amount balance)
            - The class should contain one class variable:
                - ROI (Rate of Interest), initialized to 10.5
            - Define a constructor (__init__) that accepts Name and intial Amount.
            - Implement an instance method:
                - Display() - displays account holder name and current balance.
                - Deposit() - accepts an amount from the user andd adds it to balance.
                - Withdraw() - accepts an amount from the user and substracts it from balance.
                    (Ensure withdrawal is allowed only if sufficient balance exists)
                - CalculateInterest() - calculates and returns interest using formula:
                    Interest  = (Amount * ROI) / 100
            - Create multiple objects and demonstrate all methods
---------------------------------------------------------------------------------------------------------------------
"""

class BankAccount:
    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A
        self.Amount = B

    def Display(self):
        print(f"Account Holder Name : {self.Name}")
        print(f"Your Current Balance is : {self.Amount}")

    def Deposit(self):
        print("Enter amount you want to deposit : ")
        DepositAmt = int(input())

        self.Amount = self.Amount + DepositAmt

    def Withdraw(self):
        print("Enter amount you want to withdraw : ")
        WithdrawAmt = int(input())

        if (WithdrawAmt <= self.Amount):
            self.Amount = self.Amount - WithdrawAmt
        else:
            print("You do not have sufficient balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

bobj1 = BankAccount("Shraddha", 5000000)

bobj1.Display()
bobj1.Deposit()
bobj1.Withdraw()

Ret = bobj1.CalculateInterest()
print(f"Interest : {Ret}")



"""
--------------------------------------------------------------------------------------
----------------------------------------Output----------------------------------------
--------------------------------------------------------------------------------------

Account Holder Name : Shraddha
Your Current Balance is : 5000000
Enter amount you want to deposit : 
50000
Enter amount you want to withdraw : 
10000
Interest : 529200.0

--------------------------------------------------------------------------------------

Account Holder Name : Shraddha
Your Current Balance is : 5000000
Enter amount you want to deposit : 
50000
Enter amount you want to withdraw : 
6000000
You do not have sufficient balance
Interest : 530250.0

--------------------------------------------------------------------------------------
"""