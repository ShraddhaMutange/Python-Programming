"""
--------------------------------------------------------------------------------
Problem     :   Display file contents
Description :   Write a program which accepts file name from the user, opens that file, and displays the entire contents on the console.
Author      :   Shraddha Dhananjay Mutange
Date        :   20/07/2026
--------------------------------------------------------------------------------
"""
import os

def DisplayFileContents(FileName):
    flag = False

    flag = os.path.exists(FileName)
    # flag = Path(FileName).is_file()

    if flag == False:
        print("File does not exist in given path.")
        return
    
    fobj = open(FileName, 'r')

    Data = fobj.read()

    return Data

def main():
    FileName = input("Enter file name : ")

    Ret = DisplayFileContents(FileName)

    print(Ret)
   
        

if (__name__ == "__main__"):
    main()

"""
--------------------------------------------------------------------------------
-----------------------------------Output---------------------------------------
--------------------------------------------------------------------------------

Enter file name : Demo.txt
India is my country.
Shraddha Mutange
Jay Ganesh
This is a text file.

--------------------------------------------------------------------------------

Enter file name : Hello.txt
File does not exist in given path.
None

--------------------------------------------------------------------------------
"""