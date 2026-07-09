"""
Problem : Design a Python application that creates two separate threads named EvenFactor and OddFactor.
            - Both threads should accept one integer number as a parameter.
            - The EvenFactor thread should :
                - Identify all even factors of the given number.
                - Calculate and display the sum of even factors.
            - The OddFactor thread should :
                - Identify all odd factors of the given number.
                - Calculate and display the sum of odd factors.
            - After both threads complete execution, the main thread should display the message: "Exit from main"
"""

import threading

"""
----------------------------------------------------------------------------
Function Name   :   EvenFactor
Parameters      :   Number
Description     :   Accepts N, Calculate and display the sum of even factors.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def EvenSum(N):
    Sum = 0

    print("\nEven Factors : ")
    for no in range(2, (2 * N) + 1, 2):
        if (N % no == 0 and no % 2 == 0):
            print(no)
            Sum += no

    print(f"Sum of Even factors is : {Sum}")

"""
----------------------------------------------------------------------------
Function Name   :   OddFactor
Parameters      :   Number
Description     :   Accepts N, Calculate and display the sum of odd factors.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def OddSum(N):
    Sum = 0

    print("\nOdd Factors : ")
    for no in range(1, (2 * N) + 1, 2):
        if (N % no == 0 and no % 2 == 1):
            print(no)
            Sum += no

    print(f"Sum of Odd factors is : {Sum}")

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""

def main():
    N = int(input("Enter N : "))

    EvenFactor = threading.Thread(target=EvenSum, args=(N,))
    OddFactor = threading.Thread(target=OddSum, args=(N,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter N : 10

Even Factors : 
2
10
Sum of Even factors is : 12

Odd Factors : 
1
5
Sum of Odd factors is : 6

Exit from main
----------------------------------------------------------------------------
"""