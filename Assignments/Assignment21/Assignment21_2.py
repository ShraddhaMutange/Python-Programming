"""
Problem : Design a python application that creates two threads.
            - Thread1 should calculate and display maximum element from list.
            - Thread2 should calculate and display minimum element from list.
            - The list should be accepted from user.
"""

import threading

"""
----------------------------------------------------------------------------
Function Name   :   Maximum
Parameters      :   List
Description     :   Accepts a list and displays maximum of all elements
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def Maximum(Data):
    max_no = Data[0]

    for no in Data:
        if no >= max_no:
            max_no = no

    print(f"Maximum number : {max_no}")

"""
----------------------------------------------------------------------------
Function Name   :   Minimum
Parameters      :   List
Description     :   Accepts a list and displays minimum of all elements
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def Minimum(Data):
    min_no = Data[0]

    for no in Data:
        if no <= min_no:
            min_no = no

    print(f"Minimum number : {min_no}")


"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Data = list()

    Size = int(input("Enter number of elements you want to enter : "))

    print("Enter elements : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("\nOriginal Data : ", Data)

    Max = threading.Thread(target=Maximum, args=(Data,))
    Min = threading.Thread(target=Minimum, args=(Data,))

    Max.start()
    Min.start()

    Max.join()
    Min.join()
    


if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter number of elements you want to enter : 5
Enter elements : 
21
11
51
101
18

Original Data :  [21, 11, 51, 101, 18]
Maximum number : 101
Minimum number : 11

----------------------------------------------------------------------------
"""