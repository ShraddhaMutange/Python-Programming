"""
Problem : Write a program which displays first 10 even numbers on the screen.
"""

"""
----------------------------------------------------------------------------
Function Name   : DisplayEven
Parameters      : None
Description     : Displays first 10 even numbers on the screen.
Author          : Shraddha Dhananjay Mutange
Date            : 06/07/2026
----------------------------------------------------------------------------
"""
def DisplayEven():

    for no in range(2, 2*10+1, 2):
        print(no, end=" ")

    print()

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    DisplayEven()
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
2 4 6 8 10 12 14 16 18 20 

----------------------------------------------------------------------------
"""
