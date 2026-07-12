"""
Problem : Write a program that counts how many even numbers exist between 1 and N using Pool.map().
"""

import multiprocessing
import time
import os

"""
----------------------------------------------------------------------------
Function Name   :   CountEven
Parameters      :   Number
Description     :   Accepts a number and counts all even numbers from 1 to N.
Author          :   Shraddha Dhananjay Mutange
Date            :   12/07/2026
----------------------------------------------------------------------------
"""

def CountEven(No):
    
    Count = 0

    for i in range(2, No+1, 2):
        Count = Count + 1

    print(f"\nInside Process with ID : {os.getpid()}")
    print(f"Input number is : {No}")
    print(f"Even number count : {Count}")

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

    Result = pobj.map(CountEven,Data)

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

Inside Process with ID : 14555
Input number is : 10
Odd number count : 5

Inside Process with ID : 14556
Input number is : 200000
Odd number count : 100000

Inside Process with ID : 14557
Input number is : 300000
Odd number count : 150000

Inside Process with ID : 14558
Input number is : 400000
Odd number count : 200000

The result is :  [5, 100000, 150000, 200000]

Time required is : 0.0261 seconds

------------------------------------------------------------------
"""