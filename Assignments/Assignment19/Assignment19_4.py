"""
Problem : Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return the addition of all those numbers.
"""

from functools import reduce

"""
----------------------------------------------------------------------------
Function Name   :   CheckEven
Parameters      :   Number
Description     :   Accepts a number and checks whether number is even or not.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

CheckEven = lambda No : No % 2 == 0

"""
----------------------------------------------------------------------------
Function Name   :   Square
Parameters      :   Number
Description     :   Accepts a number and returns its square.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

Square = lambda No : No ** 2

"""
----------------------------------------------------------------------------
Function Name   :   Addition
Parameters      :   Number, Number
Description     :   Accepts two numbers and returns Addition of two numbers.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

Addition = lambda No1, No2 : No1 + No2

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

    FData = list(filter(CheckEven, Data))

    print("\nFiltered Data : ", FData)

    MData = list(map(Square, FData))

    print("\nMapped Data : ", MData)

    Result = reduce(Addition, MData)

    print(f"\nOutput of Reduce is : {Result}")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter number of elements you want to enter : 10
Enter elements : 
5
2
3
4
3
4
1
2
8
10

Original Data :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

Filtered Data :  [2, 4, 4, 2, 8, 10]

Mapped Data :  [4, 16, 16, 4, 64, 100]

Output of Reduce is : 204

----------------------------------------------------------------------------
"""