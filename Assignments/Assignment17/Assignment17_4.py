"""
Problem : Write a program which accepts one number from user and return addition of its factors.

"""

"""
----------------------------------------------------------------------------
Function Name   :   SumFactors
Parameters      :   Number
Description     :   Accepts one number from user and returns addition of its factors.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def SumFactors(No):

    Sum = 0

    for i in range(1, (int(No/2)+1)):
        
        if (No % i == 0):
            Sum = Sum + i

    return Sum

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value = int(input("Enter a number : "))
    
    Ret = SumFactors(Value)
    print(f"Sum of Factors of {Value} is {Ret}")
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
Enter a number : 12
Sum of Factors of 12 is 16

----------------------------------------------------------------------------
"""
