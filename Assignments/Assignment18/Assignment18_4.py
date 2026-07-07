"""
Problem : Write a program which accept N numbers from user and store it into list. Accept one another number from the user and return the frequency of that number from the list.
"""

from functools import reduce

"""
----------------------------------------------------------------------------
Function Name   :   CountFrequency
Parameters      :   List, Number
Description     :   Accepts List and a number to be searched. Returns frequency of that number.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def CountFrequency(Data, Value):
    Count = 0

    for no in Data:
        if (no == Value):
            Count = Count + 1


    return Count

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

    print("Enter element to be searched : ")
    Value = int(input())

    Ret = CountFrequency(Data, Value)

    print(f"{Value} appeared {Ret} times in the list.")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------

Enter number of elements you want to enter : 
10
Enter 10 values : 
51
21
11
21
36
101
21
51
80
1
Enter element to be searched : 
21
21 appeared 3 times in the list.

----------------------------------------------------------------------------
"""