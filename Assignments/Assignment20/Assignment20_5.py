"""
Problem : Design a Python application that creates three separate threads named Thread1 and Thread2.
            - Thread1 should display numbers from 1 to 50.
            - Thread2 should display numbers from 50 to 1 in reverse order.
            - Ensure that:
                - Thread2 starts execution only after Thread1 has completed.
            - Use appropriate threa synchronization.
"""

import threading

"""
----------------------------------------------------------------------------
Function Name   :   Display
Parameters      :   Number
Description     :   Accepts a number and displays 1 to N.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def Display(N):
    print("Inside Display")
    for i in range(1,N + 1):
        print(i, end="\t")

    print()

"""
----------------------------------------------------------------------------
Function Name   :   ReverseDisplay
Parameters      :   Number
Description     :   Accepts a number and displays N to 1.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def ReverseDisplay(N):
    print("Inside Reverse Display")
    for i in range(N, 0, -1):
        print(i, end="\t")

    print()

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""

def main():
    N = int(input("Enter N : "))

    Thread1 = threading.Thread(target=Display, args=(N,))
    Thread2 = threading.Thread(target=ReverseDisplay, args=(N,))

    Thread1.start()
    Thread1.join()

    Thread2.start()
    

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter N : 50
Inside Display
1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	
Inside Reverse Display
50	49	48	47	46	45	44	43	42	41	40	39	38	37	36	35	34	33	32	31	30	29	28	27	26	25	24	23	22	21	20	19	18	17	16	15	14	13	12	11	10	9	8	7	6	5	4	3	21

----------------------------------------------------------------------------
"""