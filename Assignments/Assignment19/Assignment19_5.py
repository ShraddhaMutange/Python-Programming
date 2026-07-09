"""
Problem : Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers . Map function will multiply each number by 2. Reduce will return the maximum number from all those numbers.
"""

from functools import reduce

"""
----------------------------------------------------------------------------
Function Name   :   CheckPrime
Parameters      :   Number
Description     :   Accepts a number and checks whether number is prime or not.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def CheckPrime(No):
    Flag = True

    if (No <= 0):
        Flag = False
        return Flag
    
    if (No == 1 or No == 2):
        Flag = True
        return Flag

    for i in range(2, int(No/2)+1):
        if No % i == 0:
            Flag = False
            break

    return Flag


"""
----------------------------------------------------------------------------
Function Name   :   Multiply
Parameters      :   Number
Description     :   Accepts a number and multiplies it by 2.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

Multiply = lambda No : No * 2

"""
----------------------------------------------------------------------------
Function Name   :   Maximum
Parameters      :   Number, Number
Description     :   Accepts two numbers and returns maximum of two numbers.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

Maximum = lambda No1, No2 : max(No1, No2)

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Data = list()

    Size = int(input("Enter number of elements you want to enter : "))

    print("Enter elements : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("\nOriginal Data : ", Data)

    FData = list(filter(CheckPrime, Data))

    print("\nFiltered Data : ", FData)

    MData = list(map(Multiply, FData))

    print("\nMapped Data : ", MData)

    Result = reduce(Maximum, MData)

    print(f"\nOutput of Reduce is : {Result}")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter number of elements you want to enter : 5
Enter elements : 
1
2
3
4
5

Original Data :  [1, 2, 3, 4, 5]

Filtered Data :  [1, 2, 3, 5]

Mapped Data :  [2, 4, 6, 10]

Output of Reduce is : 10

----------------------------------------------------------------------------
"""