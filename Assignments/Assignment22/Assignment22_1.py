"""
Problem : Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.
"""

import multiprocessing
import time

"""
----------------------------------------------------------------------------
Function Name   :   SumSquare
Parameters      :   Number
Description     :   Accepts a number and calculate the sum of squares from 1 to N.
Author          :   Shraddha Dhananjay Mutange
Date            :   12/07/2026
----------------------------------------------------------------------------
"""

def SumSquare(No):
    sum = 0

    for i in range(1, No+1):
        sum = sum + (i ** 2)

    return sum

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""

def main():
    Data = [100000,200000,300000,400000,500000]
    Result = list()

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("The result is : ", Result)

    print(f"Time required is : {end_time - start_time:.4f} seconds")



if __name__ == "__main__":
    main()

"""
------------------------------------------------------------------
-----------------------------Output-------------------------------
------------------------------------------------------------------

The result is :  [333338333350000, 2666686666700000, 9000045000050000, 21333413333400000, 41666791666750000]
Time required is : 0.1416 seconds

------------------------------------------------------------------
"""