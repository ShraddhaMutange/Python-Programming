"""
--------------------------------------------------------------------------------
Problem     :   Check file exists in current directory
Description :   Write a program which accepts file name from the user and checks whether that file exists in the current directory
                or not.
Author      :   Shraddha Dhananjay Mutange
Date        :   20/07/2026
--------------------------------------------------------------------------------
"""
import os

def CheckFileExistanceInCurrDir(FileName):
    flag = False

    flag = os.path.exists(FileName)
    # flag = Path(FileName).is_file()

    return flag

def main():
    FileName = input("Enter file name : ")

    Ret = CheckFileExistanceInCurrDir(FileName)

    if (Ret == True):
        print("File exists in current directory.")
    else:
        print("File does not exist.")
   
        

if (__name__ == "__main__"):
    main()

"""
--------------------------------------------------------------------------------
-----------------------------------Output---------------------------------------
--------------------------------------------------------------------------------

Enter file name : Demo.txt
File exists in current directory.

--------------------------------------------------------------------------------

Enter file name : Hello.txt
File does not exist.

--------------------------------------------------------------------------------
"""