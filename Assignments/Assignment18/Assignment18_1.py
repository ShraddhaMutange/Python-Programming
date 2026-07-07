"""
Problem : Write a program which accept N numbers from user and store it into list. Return Addition of all elements from that list.
"""

from functools import reduce

"""
----------------------------------------------------------------------------
Function Name   :   Addition
Parameters      :   Number, Number
Description     :   Accepts two numbers from user and returns their addition.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def Addtion(No1, No2):
    Sum = No1 + No2
    return Sum

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

    Ans = reduce(Addtion, Data)

    print(f"Addition of all elements is : {Ans}")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------

Enter number of elements you want to enter : 
5
Enter 5 values : 
1
2
3
4
5
Addition of all elements is : 15

----------------------------------------------------------------------------
"""