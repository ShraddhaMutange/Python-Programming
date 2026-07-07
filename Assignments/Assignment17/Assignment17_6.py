"""
Problem : Write a program which accepts one number from user and displays below pattern.
Input : 5
Output : 
    *   *   *   *   *
    *   *   *   *   
    *   *   *   
    *   *   
    *   

"""

"""
----------------------------------------------------------------------------
Function Name   :   Display
Parameters      :   Number
Description     :   Accepts one number from user and displays below pattern.
                    Input : 5
                    Output : 
                        *   *   *   *   *
                        *   *   *   *   
                        *   *   *   
                        *   *   
                        *   
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def Display(No):

    for i in range(No, 0, -1):
        for j in range(i):
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
* * * * 
* * * 
* * 
* 

----------------------------------------------------------------------------
"""
