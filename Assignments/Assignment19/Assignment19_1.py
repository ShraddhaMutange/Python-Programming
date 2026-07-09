"""
Problem : Write a program which contains one lambda function which accepts  parameter and return power of two.
"""

"""
----------------------------------------------------------------------------
Function Name   :   PowerOfTwo
Parameters      :   Number
Description     :   Accepts a number and returns power of two of that number.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

PowerOfTwo = lambda No : No ** 2

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    print("Enter a number : ")
    Value = int(input())

    Ret = PowerOfTwo(Value)
    
    print(f"2 to the power of {Value} is : {Ret}")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter a number : 
10
2 to the power of 10 is : 100

----------------------------------------------------------------------------

Enter a number : 
2
2 to the power of 2 is : 4

----------------------------------------------------------------------------

Enter a number : 
-2
2 to the power of -2 is : 4

----------------------------------------------------------------------------
"""