"""
Problem : Design a Python application that creates two separate threads named even and odd.
            - The even thread should display the first 10 even numbers.
            - The odd thread should display the first 10 odd numbers.
            - Both threads should execute independently using the threading module.
            - Ensure proper thread creation and execution.
"""

import threading

"""
----------------------------------------------------------------------------
Function Name   :   DisplayEven
Parameters      :   Number
Description     :   Accepts N and displays N even numbers.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def DisplayEven(N):
    print("Even Numbers :")
    for no in range(2,(2*N)+1,2):
        print(no)

"""
----------------------------------------------------------------------------
Function Name   :   DisplayOdd
Parameters      :   Number
Description     :   Accepts N and displays N odd numbers.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def DisplayOdd(N):
    print("Odd Numbers :")
    for no in range(1,(2*N)+1,2):
        print(no)

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    N = int(input("Enter N : "))

    Even = threading.Thread(target=DisplayEven, args=(N,))
    Odd = threading.Thread(target=DisplayOdd, args=(N,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()



if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter N : 10
Even Numbers :
2
4
6
8
10
12
14
16
18
Odd Numbers :
1
3
20
5
7
9
11
13
15
17
19

----------------------------------------------------------------------------
"""