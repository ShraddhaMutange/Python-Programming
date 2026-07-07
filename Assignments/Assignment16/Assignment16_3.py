"""
Problem : Write a program which contains one function named as Add() which accepts two numbers from users and returns addition of those two numbers.
"""

"""
----------------------------------------------------------------------------
Function Name   : Add
Parameters      : Number, Number
Return Type     : Number
Description     : Returns addtion of two numbers.
Author          : Shraddha Dhananjay Mutange
Date            : 06/07/2026
----------------------------------------------------------------------------
"""
def Add(No1,No2):
    Sum = No1 + No2
    return Sum  

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    
    Ret = Add(Value1, Value2)

    print("Addition is :", Ret)

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
Enter first number : 10
Enter second number : 11
Addition is : 21
----------------------------------------------------------------------------
"""
