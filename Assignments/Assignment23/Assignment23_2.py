"""
Problem : Write a program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N for every number from the given list.
"""

import multiprocessing
import time
import os

"""
----------------------------------------------------------------------------
Function Name   :   SumOdd
Parameters      :   Number
Description     :   Accepts a number and calculate the sum of all odd numbers from 1 to N.
Author          :   Shraddha Dhananjay Mutange
Date            :   12/07/2026
----------------------------------------------------------------------------
"""

def SumOdd(No):
    
    sum = 0

    for i in range(1, No+1, 2):
        sum = sum + i

    print(f"\nInside Process with ID : {os.getpid()}")
    print(f"Input number is : {No}")
    print(f"Sum of Odd numbers : {sum}")

    return sum

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""

def main():
    Data = [10,200000,300000,400000]
    Result = list()

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("\nThe result is : ", Result)

    print(f"\nTime required is : {end_time - start_time:.4f} seconds")



if __name__ == "__main__":
    main()

"""
------------------------------------------------------------------
-----------------------------Output-------------------------------
------------------------------------------------------------------

Inside Process with ID : 12839
Input number is : 10
Sum of Even numbers : 25

Inside Process with ID : 12840
Input number is : 200000
Sum of Even numbers : 10000100000

Inside Process with ID : 12841
Input number is : 300000
Sum of Even numbers : 22500150000

Inside Process with ID : 12842
Input number is : 400000
Sum of Even numbers : 40000200000

The result is :  [2500050000, 10000100000, 22500150000, 40000200000]

Time required is : 0.0266 seconds

------------------------------------------------------------------
"""