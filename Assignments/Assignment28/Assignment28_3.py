"""
--------------------------------------------------------------------------------
Problem     : Display file line by line
Description : Write a program which accepts file name from the user and displays the contents of the file line by line on the screen.
Author      : Shraddha Dhananjay Mutange
Date        : 19/07/2026
--------------------------------------------------------------------------------
"""

def main():
    fname = input("Enter file name : ")

    try:
            
        fobj = open(fname, 'r')

        print("File Content :")
        for line in fobj:
            print(f"\t{line}")
        

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
File Content :
	Jay Ganesh...

	Marvellous Infosystems

	Shraddha Mutange

	India is my country

--------------------------------------------------------------------------------
"""