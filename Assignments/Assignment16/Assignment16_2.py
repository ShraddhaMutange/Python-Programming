"""
Problem : Write a program which contains one function named as CheckNum() which accepts a number and return "Even number" if the number is even otherwise returns "Odd number".
"""

"""
----------------------------------------------------------------------------
Function Name   : CheckNum
Parameters      : Number
Description     : Displays "Even number" if a number is even otherwise "Odd number".
Author          : Shraddha Dhananjay Mutange
Date            : 06/07/2026
----------------------------------------------------------------------------
"""
def CheckEven(No):
    return (No % 2 == 0)    

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value = int(input("Enter a number : "))
    
    Ret = CheckEven(Value)

    if Ret == True:
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
Enter a number : 10
Even Number
----------------------------------------------------------------------------
Enter a number : 11
Odd Number
----------------------------------------------------------------------------
"""
