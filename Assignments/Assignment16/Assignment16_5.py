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
def CheckNumber():

    for no in range(10, 0, -1):
        print(no, end="\t")
    print()

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    CheckNumber()
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
10	9	8	7	6	5	4	3	2	1
----------------------------------------------------------------------------
"""
