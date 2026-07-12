"""
Problem : Write a program that counts how many odd numbers exist between 1 and N using Pool.map().
"""

import multiprocessing
import time
import os

"""
----------------------------------------------------------------------------
Function Name   :   CountOdd
Parameters      :   Number
Description     :   Accepts a number and counts all odd numbers from 1 to N.
Author          :   Shraddha Dhananjay Mutange
Date            :   12/07/2026
----------------------------------------------------------------------------
"""

def CountOdd(No):
    
    Count = 0

    for i in range(1, No+1, 2):
        Count = Count + 1

    print(f"\nInside Process with ID : {os.getpid()}")
    print(f"Input number is : {No}")
    print(f"Odd number count : {Count}")

    return Count

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

    Result = pobj.map(CountOdd,Data)

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

Inside Process with ID : 14411
Input number is : 10
Even number count : 5

Inside Process with ID : 14412
Input number is : 200000
Even number count : 100000

Inside Process with ID : 14413
Input number is : 300000
Even number count : 150000

Inside Process with ID : 14414
Input number is : 400000
Even number count : 200000

The result is :  [5, 100000, 150000, 200000]

Time required is : 0.0254 seconds

------------------------------------------------------------------
"""