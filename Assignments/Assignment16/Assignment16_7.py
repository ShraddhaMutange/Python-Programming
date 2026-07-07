"""
Problem : Write a lambda function which accepts one number and returns True if number is even otherwise False.
"""

"""
----------------------------------------------------------------------------
Function Name   : DivBy5
Parameters      : Number
Description     : Checks whether number is positive, negative or zero.
Author          : Shraddha Dhananjay Mutange
Date            : 06/07/2026
----------------------------------------------------------------------------
"""
def DivBy5(No): 
    return (No % 5 == 0)

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value = int(input("Enter a number : "))

    Ret = DivBy5(Value)
    print(Ret)


if (__name__ == "__main__"):
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------

Enter a number : 15
True

-----------------------------------------

Enter a number : 14
False

----------------------------------------------------------------------------
"""
