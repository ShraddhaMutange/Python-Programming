"""
Problem : For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.
"""

import multiprocessing
import time

"""
----------------------------------------------------------------------------
Function Name   :   CheckPrime
Parameters      :   Number
Description     :   Accepts a number and checks whether number is prime or not.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def CheckPrime(No):
    Flag = True

    if (No <= 0):
        Flag = False
        return Flag
    
    if (No == 1 or No == 2):
        Flag = True
        return Flag

    for i in range(2, int(No/2)+1):
        if No % i == 0:
            Flag = False
            break

    return Flag

"""
----------------------------------------------------------------------------
Function Name   :   CountPrime
Parameters      :   Number
Description     :   Accepts a number and count how many prime numbers exist between 1 and N.
Author          :   Shraddha Dhananjay Mutange
Date            :   12/07/2026
----------------------------------------------------------------------------
"""

def CountPrime(No):
    Count = 0

    for i in range(1,No+1):
        if (CheckPrime(i) == True):
            Count = Count + 1

    return Count
    

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

    Result = pobj.map(CountPrime, Data)

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

Result is :  [1230, 2263, 3246, 4204]
Time required is : 3.7806

------------------------------------------------------------------
"""