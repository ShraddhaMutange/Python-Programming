"""
Problem : Design a Python application that creates two separate threads named EvenList and OddList.
            - Both threads should accept a list of integers as input.
            - The EvenList thread should :
                - Extract all even elements from the list.
                - Calculate and display their sum.
            - The OddList thread should :
                - Extract all odd elements from the list.
                - Calculate and display their sum.
            - Threads should run concurrently.
"""

import threading

"""
----------------------------------------------------------------------------
Function Name   :   EvenSum
Parameters      :   Number
Description     :   Accepts N, Calculate and display the sum of even factors.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def EvenSum(Data):
    Sum = 0

    print("\nEven elements list : ")
    for no in Data:
        if (no % 2 == 0):
            print(no)
            Sum += no

    print(f"Sum of Even elements is : {Sum}")

"""
----------------------------------------------------------------------------
Function Name   :   OddSum
Parameters      :   Number
Description     :   Accepts N, Calculate and display the sum of odd factors.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def OddSum(Data):
    Sum = 0

    print("\nOdd elements list : ")
    for no in Data:
        if (no % 2 == 1):
            print(no)
            Sum += no

    print(f"Sum of Odd elements is : {Sum}")

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""

def main():
    Size = int(input("Enter size of list : "))
    Data = list()

    print("\nEnter elements :")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("\nEntered Data : ", Data)

    EvenList = threading.Thread(target=EvenSum, args=(Data,))
    OddList = threading.Thread(target=OddSum, args=(Data,))

    EvenList.start()
    OddList.start()




if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter size of list : 10

Enter elements :
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

Entered Data :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Even elements list : 
2
4
6
8
10
Sum of Even elements is : 30

Odd elements list : 
1
3
5
7
9
Sum of Odd elements is : 25

----------------------------------------------------------------------------
"""