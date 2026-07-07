"""
Problem : Write a program which accepts one number from user and return addition of digits in that number.
Input : 5187964
Output : 7

"""

"""
----------------------------------------------------------------------------
Function Name   :   SumDigits
Parameters      :   Number
Description     :   Accepts one number from user and return addition of digits in that number.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def SumDigits(No):

    Digit = 0
    Sum = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = int(No / 10)

    return Sum

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value = int(input("Enter a number : "))
    
    Ret = SumDigits(Value)

    print(f"Sum of digits in {Value} is : {Ret}")
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------

Enter a number : 5187934
Sum of digits in 5187934 is : 37

----------------------------------------------------------------------------

Enter a number : 12345
Sum of digits in 12345 is : 15

----------------------------------------------------------------------------
"""
