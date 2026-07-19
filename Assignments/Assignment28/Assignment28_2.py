"""
--------------------------------------------------------------------------------
Problem     : Count words in a file
Description : Write a program which accepts file name from the user and counts how many words are present in the file. 
Author      : Shraddha Dhananjay Mutange
Date        : 19/07/2026
--------------------------------------------------------------------------------
"""

def main():
    fname = input("Enter file name : ")

    try:
            
        fobj = open(fname, 'r')

        count = 0

        for line in fobj:
            words = line.split()
            count = count + len(words)
        
        print("Total number of words : ", count)

        fobj.close()

    except FileNotFoundError as eobj:
        print("Error occured : ", eobj)

    except Exception as eobj:
        print("Error occured : ", eobj)

if (__name__ == "__main__"):
    main()

"""
--------------------------------------------------------------------------------
-----------------------------------Output---------------------------------------
--------------------------------------------------------------------------------

Enter file name : Demo  
Error occured :  [Errno 2] No such file or directory: 'Demo'

--------------------------------------------------------------------------------

Enter file name : DemoFile.txt
Total number of words :  10

--------------------------------------------------------------------------------
"""