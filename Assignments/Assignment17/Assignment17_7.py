"""
Problem : Write a program which accepts one number from user and displays below pattern.
Input : 5
Output : 
    1   2   3   4   5
    1   2   3   4   5
    1   2   3   4   5
    1   2   3   4   5
    1   2   3   4   5

"""

"""
----------------------------------------------------------------------------
Function Name   :   Display
Parameters      :   Number
Description     :   Accepts one number from user and displays below pattern.
                    Input : 5
                    Output : 
                        1   2   3   4   5
                        1   2   3   4   5
                        1   2   3   4   5
                        1   2   3   4   5
                        1   2   3   4   5
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def Display(No):

    for i in range(1, No+1):
        for j in range(1, No+1):
            print(j, end="\t")

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
1	2	3	4	5	
1	2	3	4	5	
1	2	3	4	5	
1	2	3	4	5	
1	2	3	4	5

----------------------------------------------------------------------------
"""
