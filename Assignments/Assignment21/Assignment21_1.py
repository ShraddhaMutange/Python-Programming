"""
Problem : Design a python application that creates two threads named Prime and NonPrime.
            - Both threads should accept a list of integers.
            - The Prime thread should display all prime numbers from the list.
            - The NonPrime thread should display all non-prime numbers from the list.
"""

import threading

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

def PrimeNumbers(Data):
    Result = list()

    for no in Data:
        if (CheckPrime(no) == True):
            Result.append(no)

    print("Prime numbers : ", Result)

def NonPrimeNumbers(Data):
    Result = list()

    for no in Data:
        if (CheckPrime(no) == False):
            Result.append(no)

    print("Non prime numbers : ", Result)


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

    Prime = threading.Thread(target=PrimeNumbers, args=(Data,))
    NonPrime = threading.Thread(target=NonPrimeNumbers, args=(Data,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()
    


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter number of elements you want to enter : 10
Enter elements : 
11
12
13
14
15
16
17
18
19
20

Original Data :  [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Prime numbers :  [11, 13, 17, 19]
Non prime numbers :  [12, 14, 15, 16, 18, 20]

----------------------------------------------------------------------------
"""