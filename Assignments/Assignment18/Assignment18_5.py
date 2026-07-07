"""
Problem : Write a program which accept N numbers from user and store it into list. Return addition of all prime numbers from that list. Main python file accepts N  numbers from user and pass each number to CheckPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from aminpython file should be ListPrime().
"""

from functools import reduce

"""
----------------------------------------------------------------------------
Function Name   :   CheckPrime
Parameters      :   Number
Description     :   Accepts a number and check whether it is prime or not.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def CheckPrime(No):
    # print("Inside CheckPrime")
    Flag = True

    if No <= 0:
        return False

    if No == 1 or No == 2:
        return True

    for i in range(2, (int(No/2)+1)):
        if (No % i == 0):
            Flag = False
            break

    return Flag

"""
----------------------------------------------------------------------------
Function Name   :   ListPrime
Parameters      :   List
Description     :   Accepts List of numbers and returns list of prime numbers.
Author          :   Shraddha Dhananjay Mutange
Date            :   06/07/2026
----------------------------------------------------------------------------
"""
def ListPrime(Data):
    # print("Inside ListPrime")

    # Resul = list()

    # for no in Data:
    #     if (CheckPrime(no) == True):
    #         Result.append(no)

    FData = list(filter(CheckPrime, Data))
    # print(FData)

    return FData

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

    print("Entered Data is : ", Data)

    PrimeListData = ListPrime(Data)

    print("Prime Numbers : ",PrimeListData)

    AdditionOfPrimes = reduce(Addtion, PrimeListData)

    print(f"Addition of prime numbers is : {AdditionOfPrimes}")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------

Enter number of elements you want to enter : 
10
Enter 10 values : 
1
2
3
4
5
6
7
8
9
10
Entered Data is :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Prime Numbers :  [1, 2, 3, 5, 7]
Addition of prime numbers is : 18

----------------------------------------------------------------------------

Enter number of elements you want to enter : 
11
Enter 11 values : 
13
5
45
7
4
56
10
34
2
5
8
Entered Data is :  [13, 5, 45, 7, 4, 56, 10, 34, 2, 5, 8]
Prime Numbers :  [13, 5, 7, 2, 5]
Addition of prime numbers is : 32
----------------------------------------------------------------------------
"""