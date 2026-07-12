"""
Problem : Write a program that calculates : 1^5 + 2^5 + 3^5 + ... + N^5 for multiple numbers simultaneously using Pool. And measure total execution time.
"""

import multiprocessing
import time

"""
----------------------------------------------------------------------------
Function Name   :   Calculate
Parameters      :   Number
Description     :   Accepts a number and calculates : 1^5 + 2^5 + 3^5 + ... + N^5.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def Calculate(No):
    Ans = 0

    for i in range(1, No+1):
        Ans = Ans + (i ** 5)

    return Ans

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""

def main():
    Data = [10000,20000,30000,40000]
    Result = list()

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Calculate, Data)

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

Result is :  [166716670833333325000000, 10668266733333333300000000, 121512150337499999925000000, 682717867733333333200000000]
Time required is : 0.0231

------------------------------------------------------------------
"""