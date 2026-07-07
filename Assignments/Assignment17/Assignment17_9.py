"""
Problem : Write a program which accepts one number from user and return number of digits in that number.
Input : 5187964
Output : 7

"""

"""
----------------------------------------------------------------------------
Function Name   :   CountDigits
Parameters      :   Number
Description     :   Accepts one number from user and return number of digits in that number.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def CountDigits(No):

    # Digit = 0
    Count = 0

    while(No != 0):
        # Digit = No % 10
        Count = Count + 1
        No = int(No / 10)

    return Count

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value = int(input("Enter a number : "))
    
    Ret = CountDigits(Value)

    print(f"Number of digits in {Value} is : {Ret}")
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------

Enter a number : 12345
Number of digits in 12345 is : 5

----------------------------------------------------------------------------

Enter a number : 5187955
Number of digits in 5187955 is : 7

----------------------------------------------------------------------------
"""
