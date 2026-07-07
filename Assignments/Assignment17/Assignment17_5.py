"""
Problem : Write a program which accepts one number from user and check whether it is prime or not.

"""

"""
----------------------------------------------------------------------------
Function Name   :   CheckPrime
Parameters      :   Number
Description     :   Accepts one number from user and check whether it is prime or not.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def CheckPrime(No):

    Flag = True

    if No == 0:
        return False

    if No == 1 or No == 2:
        return True

    for i in range(2, (int(No/2)+1)):
        if(No % i == 0):
            Flag = False
            break

    return Flag

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value = int(input("Enter a number : "))
    
    Ret = CheckPrime(Value)
    
    if Ret == True:
        print(f"{Value} is a Prime number")
    else:
        print(f"{Value} is not a Prime number")
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter a number : 0
0 is not a Prime number

----------------------------------------------------------------------------

Enter a number : 1
1 is a Prime number

----------------------------------------------------------------------------

Enter a number : 2
2 is a Prime number

----------------------------------------------------------------------------

Enter a number : 3
3 is a Prime number

----------------------------------------------------------------------------

Enter a number : 4
4 is not a Prime number

----------------------------------------------------------------------------

Enter a number : 5
5 is a Prime number

----------------------------------------------------------------------------

Enter a number : 17
17 is a Prime number

----------------------------------------------------------------------------

Enter a number : 21
21 is not a Prime number

----------------------------------------------------------------------------
"""
