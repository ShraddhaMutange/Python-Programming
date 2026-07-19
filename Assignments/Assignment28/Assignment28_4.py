"""
--------------------------------------------------------------------------------
Problem     :   Copy file contents into another file
Description :   Write a program which accepts two file names from the user.
                - First file is an existing file
                - Second file is a new file
                Copy all contents from the first file into the second file.
Author      : Shraddha Dhananjay Mutange
Date        : 19/07/2026
--------------------------------------------------------------------------------
"""

def main():
    sfname = input("Enter source file name : ")
    dfname = input("Enter destination file name : ")


    try:
            
        sfobj = open(sfname, 'r')
        dfobj = open(dfname, 'w')

        for line in sfobj:
            dfobj.write(line)

        print(f"File content of {sfname} copied successfully into {dfname} file.")


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

Enter source file name : DemoFile.txt
Enter destination file name : DestinationFile.txt
File content of DemoFile.txt copied successfully into DestinationFile.txt file.

--------------------------------------------------------------------------------
"""