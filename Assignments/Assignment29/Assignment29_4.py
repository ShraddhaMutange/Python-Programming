"""
--------------------------------------------------------------------------------
Problem     :   Copy File Contents into a New file (Command line)
Description :   Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.
Author      :   Shraddha Dhananjay Mutange
Date        :   20/07/2026
--------------------------------------------------------------------------------
"""
import os
import sys

def CopyFileContent(SrcFileName, DestFileName="DemoDest.txt"):
    
    if (os.path.exists(SrcFileName) == False):
        print("This file does not exist in given path.")
        return
    
    src_fobj = open(SrcFileName, 'r')
    dest_fobj = open(DestFileName, 'w')

    Buffer = src_fobj.read(1024)

    while(len(Buffer) > 0):
        dest_fobj.write(Buffer)
        Buffer = src_fobj.read(1024)

    print(f"Succesfully copied contents fron {SrcFileName} into {DestFileName}")

    src_fobj.close()
    dest_fobj.close()


def main():
    # sys.argv[0] is the script name. sys.argv[1] is the source file.
    # Total arguments needed is 2.
    
    if (len(sys.argv) == 2 or len(sys.argv) == 3):
        CopyFileContent(sys.argv[1])
    else:
        print("InvalidCommandError : Pass command line arguments such as : FileName, SourceFileName DestinationFileName")

   
        

if (__name__ == "__main__"):
    main()

"""
--------------------------------------------------------------------------------
-----------------------------------Output---------------------------------------
--------------------------------------------------------------------------------

Succesfully copied contents fron Demo.txt into DemoDest.txt

--------------------------------------------------------------------------------

InvalidCommandError : Pass command line arguments such as : FileName, SourceFileName DestinationFileName


--------------------------------------------------------------------------------
"""