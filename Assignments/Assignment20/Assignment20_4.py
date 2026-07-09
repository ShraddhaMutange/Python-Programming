"""
Problem : Design a Python application that creates three separate threads named Thread1 and Thread2.
            - All threads should accept a string as an input.
            - The Small thread should count and display the number of lowercase characters.
            - The Capital thread should count and display the number of uppercase characters.
            - The Digits thread should count and display the number of numeric digits.
            - Each thread must display:
                - Thread ID
                - Thread Name
"""

import threading

"""
----------------------------------------------------------------------------
Function Name   :   Lowercase
Parameters      :   String
Description     :   Accepts string and counts number of lowercase characters.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def Lowercase(Data):
    Count = 0

    for ch in Data:
        if 'a' <= ch <= 'z':
            Count += 1

    print(f"Number of lower case characters is : {Count}")


"""
----------------------------------------------------------------------------
Function Name   :   Uppercase
Parameters      :   String
Description     :   Accepts string and counts number of Uppercase characters.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def Uppercase(Data):
    Count = 0

    for ch in Data:
        if 'A' <= ch <= 'Z':
            Count += 1

    print(f"Number of upper case characters is : {Count}")

"""
----------------------------------------------------------------------------
Function Name   :   Numerics
Parameters      :   String
Description     :   Accepts string and counts number of Numerics digits.
Author          :   Shraddha Dhananjay Mutange
Date            :   07/07/2026
----------------------------------------------------------------------------
"""

def Numerics(Data):
    Count = 0

    for ch in Data:
        if '0' <= ch <= '9':
            Count += 1

    print(f"Number of digits is : {Count}")

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""

def main():
    str = input("Enter a string : ")

    print("\nEntered String : ", str)

    Small = threading.Thread(target=Lowercase, args=(str,))
    Capital = threading.Thread(target=Uppercase, args=(str,))
    Digits = threading.Thread(target=Numerics, args=(str,))    

    Small.start()
    Capital.start()
    Digits.start()

if __name__ == "__main__":
    main()

"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter a string : ShrADDha2005

Entered String :  ShrADDha2005
Number of lower case characters is : 4
Number of upper case characters is : 4
Number of digits is : 4

----------------------------------------------------------------------------
"""