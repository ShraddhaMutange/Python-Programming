"""
--------------------------------------------------------------------------------
Problem     :   Compare two files (Command line)
Description :   Write a program which accepts two file names through command line arguments and compares the content of both files.
                - If both files contain the same contents, display Success
                - Otherwise fisplay Failure
Author      :   Shraddha Dhananjay Mutange
Date        :   20/07/2026
--------------------------------------------------------------------------------
"""
import os
import sys
import hashlib

def CalculateChecksum(FileName):
    if (os.path.exists(FileName) == False):
        print(f"{FileName} file does not exist in given path.")
        return    
    
    hobj = hashlib.md5()

    fobj = open(FileName, 'rb')

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def CompareFiles(fname1, fname2):
    file1_checksum = CalculateChecksum(fname1)
    file2_checksum = CalculateChecksum(fname2)

    return file1_checksum == file2_checksum 


def main():
    # sys.argv[0] is the script name. sys.argv[1] is the source file.
    # Total arguments needed is 2.
    
    if (len(sys.argv) == 3):
        Ret = CompareFiles(sys.argv[1], sys.argv[2])

        if (Ret == True):
            print("SUCCESS")
        else:
            print("FAILURE")

    else:
        print("InvalidCommandError : Pass command line arguments such as : FileName.py, FileName1 FileName2")


if (__name__ == "__main__"):
    main()

"""
--------------------------------------------------------------------------------
-----------------------------------Output---------------------------------------
--------------------------------------------------------------------------------

$ python3 Assignment29_4.py
InvalidCommandError : Pass command line arguments such as : FileName.py, FileName1 FileName2

--------------------------------------------------------------------------------

$ python3 Assignment29_4.py Demo.txt DemoCopy.txt
DemoCopy.txt file does not exist in given path.
FAILURE

--------------------------------------------------------------------------------

$ python3 Assignment29_4.py Demo.txt DemoDest.txt
SUCCESS

--------------------------------------------------------------------------------

$ python3 Assignment29_4.py Demo.txt Assignment29_2.py
FAILURE

--------------------------------------------------------------------------------
"""