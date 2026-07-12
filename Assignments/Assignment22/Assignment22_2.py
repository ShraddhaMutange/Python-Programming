"""
Problem : Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().
"""

import multiprocessing
import time

"""
----------------------------------------------------------------------------
Function Name   :   Factorial
Parameters      :   Number
Description     :   Accepts a number and calculate its factorial.
Author          :   Shraddha Dhananjay Mutange
Date            :   12/07/2026
----------------------------------------------------------------------------
"""

def Factorial(No):
    Fact = 1

    for i in range(1, No+1):
        Fact = Fact * i


    return Fact

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""

def main():
    Data = [10,15,20,25,30]
    Result = list()

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is : ", Result)

    print(f"Time required is : {end_time - start_time:.4f}")



if __name__ == "__main__":
    main()

"""
------------------------------------------------------------------
-----------------------------Output-------------------------------
------------------------------------------------------------------

Result is :  [3628800, 1307674368000, 2432902008176640000, 15511210043330985984000000, 265252859812191058636308480000000]
Time required is : 0.0653

------------------------------------------------------------------
"""