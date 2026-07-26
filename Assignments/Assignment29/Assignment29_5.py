"""
--------------------------------------------------------------------------------
Problem     :   Frequency of a string in file
Description :   Write a program which accepts a file name and one string from the user and returns the frequency (count of occurences) of that string in the file.
Author      :   Shraddha Dhananjay Mutange
Date        :   20/07/2026
--------------------------------------------------------------------------------
"""
import os
import sys
import hashlib

def CalculateFrequency(FileName, target_string):
    if (os.path.exists(FileName) == False):
        print(f"{FileName} file does not exist in given path.")
        return 
    
    fobj = open(FileName, 'r')

    Data = fobj.read()

    Frequency = Data.count(target_string)

    return Frequency
     

def main():
    fname = input("Enter file name : ")
    str = input("Enter string : ")

    Ret = CalculateFrequency(fname, str)

    print(f"Frequency of '{str}' in {fname} is : {Ret}")


if (__name__ == "__main__"):
    main()

"""
--------------------------------------------------------------------------------
-----------------------------------Output---------------------------------------
--------------------------------------------------------------------------------

Enter file name : Demo.txt
Enter string : Shraddha
Frequency of 'Shraddha' in Demo.txt is : 4

--------------------------------------------------------------------------------

Enter file name : Demo.txt
Enter string : in
Frequency of 'in' in Demo.txt is : 0

--------------------------------------------------------------------------------
"""