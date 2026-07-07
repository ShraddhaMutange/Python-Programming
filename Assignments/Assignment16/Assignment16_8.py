"""
Problem : Write a program which accepts a number from user and print that number of "*" on the screen.
"""

"""
----------------------------------------------------------------------------
Function Name   : Display
Parameters      : Number
Description     : Accepts a number from user and print that number of "*" on the screen.
Author          : Shraddha Dhananjay Mutange
Date            : 06/07/2026
----------------------------------------------------------------------------
"""
def Display(No):

    for no in range(5):
        print("*", end=" ")

    print()

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value = int(input("Enter a number : "))
    Display(Value)
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
Enter a number : 5
* * * * * 

----------------------------------------------------------------------------
"""
