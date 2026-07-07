"""
Problem : Write a program which accept N numbers from user and store it into list. Return minimum number from that list.
"""

from functools import reduce

"""
----------------------------------------------------------------------------
Function Name   :   Maximum
Parameters      :   Number, Number
Description     :   Accepts two numbers from user and returns minimum.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def Minimum(No1, No2):
    Min = min(No1, No2)
    return Min

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    print("Enter number of elements you want to enter : ")
    Size = int(input())
    Data = list()

    print(f"Enter {Size} values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    Ans = reduce(Minimum, Data)

    print(f"Minimum of all elements is : {Ans}")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------

Enter number of elements you want to enter : 
5
Enter 5 values : 
21
11
101
51
18
Minimum of all elements is : 11

----------------------------------------------------------------------------
"""