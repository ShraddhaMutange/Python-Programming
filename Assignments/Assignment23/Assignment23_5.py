"""
Problem : Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.pool.
"""

import multiprocessing
import time
import os

"""
----------------------------------------------------------------------------
Function Name   :   Factorial
Parameters      :   Number
Description     :   Accepts a number and calculates its factorials.
Author          :   Shraddha Dhananjay Mutange
Date            :   12/07/2026
----------------------------------------------------------------------------
"""

def Factorial(No):
    Fact = 1
    
    for i in range(1,No+1):
        Fact = Fact * i

    print(f"\nInside Process with ID : {os.getpid()}")
    print(f"Input number : {No}")
    print(f"Factorial : {Fact}")

    return Fact


"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""

def main():
    Data = [10,15,20,25]
    Result = list()

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial,Data)

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

Inside Process with ID : 18950
Input number : 10
Factorial : 3628800

Inside Process with ID : 18951
Input number : 15
Factorial : 1307674368000

Inside Process with ID : 18952
Input number : 20
Factorial : 2432902008176640000

Inside Process with ID : 18953
Input number : 25
Factorial : 15511210043330985984000000

The result is :  [3628800, 1307674368000, 2432902008176640000, 15511210043330985984000000]

Time required is : 0.0223 seconds

------------------------------------------------------------------
"""