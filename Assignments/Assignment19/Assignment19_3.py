"""
Problem : Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return the product of all those numbers.
"""

from functools import reduce

"""
----------------------------------------------------------------------------
Function Name   :   CheckNumber
Parameters      :   Number
Description     :   Accepts a number and checks whether number is greater than or equal to 70 and less than or equal to 90.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

CheckNumber = lambda No : 70 <= No <= 90

"""
----------------------------------------------------------------------------
Function Name   :   Increament
Parameters      :   Number
Description     :   Accepts a number and increaments it by 10.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

Increament = lambda No : No + 10

"""
----------------------------------------------------------------------------
Function Name   :   Multiplication
Parameters      :   Number, Number
Description     :   Accepts two numbers and returns their product.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

Multiplication = lambda No1, No2 : No1 * No2

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

    FData = list(filter(CheckNumber, Data))

    print("\nFiltered Data : ", FData)

    MData = list(map(Increament, FData))

    print("\nMapped Data : ", MData)

    Result = reduce(Multiplication, MData)

    print(f"\nMultiplication is : {Result}")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter number of elements you want to enter : 12
Enter elements : 
4
34
36
76
68
24
89
23
86
90
45
70

Original Data :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

Filtered Data :  [76, 89, 86, 90, 70]

Mapped Data :  [86, 99, 96, 100, 80]

Multiplication is : 6538752000

----------------------------------------------------------------------------
"""