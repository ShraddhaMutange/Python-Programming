"""
Problem : Write a program which accepts one number from user and return its factorial.
Input : 5
Output : 120

"""

"""
----------------------------------------------------------------------------
Function Name   :   Factorial
Parameters      :   Number
Description     :   Accepts one number from user and returns its factorial.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def Factorial(No):

    Fact = 1

    for i in range(1, No+1):
        Fact = Fact * i

    return Fact

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value = int(input("Enter a number : "))
    
    Ret = Factorial(Value)
    print(f"Factorial of {Value} is {Ret}")
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
Enter a number : 5
Factorial of 5 is 120

----------------------------------------------------------------------------
"""
