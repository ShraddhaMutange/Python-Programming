"""
Problem : Write a program which contains one lambda function which accepts two parameters and return its multiplication.
"""

"""
----------------------------------------------------------------------------
Function Name   :   Multiplication
Parameters      :   Number
Description     :   Accepts a number and returns power of two of that number.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

Multiplication = lambda No1, No2 : No1 * No2

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Multiplication(Value1, Value2)
    
    print(f"{Value1} * {Value2} = {Ret}")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter first number : 
10
Enter second number : 
11
10 * 11 = 110

----------------------------------------------------------------------------

Enter first number : 
4
Enter second number : 
3
4 * 3 = 12

----------------------------------------------------------------------------
"""