"""
Problem : Write a program which accepts name from user and displays length of that name.
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
def CalLength(name):

    name_len = len(name)

    return name_len

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Name = input("Enter name : ")

    Ret = CalLength(Name)
    print(f"Length of {Name} is : {Ret}")
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
Enter name : shraddha
Length of shraddha is : 8

----------------------------------------------------------------------------

Enter name : jay ganesh
Length of jay ganesh is : 10

----------------------------------------------------------------------------
"""
