"""
Problem : Write a program which accepts a number from user and check whether that number is positive, negative or zero.
"""

"""
----------------------------------------------------------------------------
Function Name   : CheckNumber
Parameters      : Number
Description     : Checks whether number is positive, negative or zero.
Author          : Shraddha Dhananjay Mutange
Date            : 06/07/2026
----------------------------------------------------------------------------
"""
def CheckNumber(No):
    if(No == 0):
        print("Zero")
    elif(No > 0):
        print("Positive Number")
    else:
        print("Negative Number")
    

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value = int(input("Enter a number : "))

    CheckNumber(Value)
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------

Enter a number : 5
Positive Number

----------------------------------------------------------------------------

Enter a number : -5
Negative Number

----------------------------------------------------------------------------

Enter a number : 0
Zero

----------------------------------------------------------------------------
"""
