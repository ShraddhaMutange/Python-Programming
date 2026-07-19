"""
--------------------------------------------------------------------------------
Problem     : Search a word in a file
Description : Write a program which accepts file name and a word from the user and checks whether that word is present in the file or not.
Author      : Shraddha Dhananjay Mutange
Date        : 19/07/2026
--------------------------------------------------------------------------------
"""

def main():
    fname = input("Enter file name : ")
    search_word = input("Enter word you want to search : ")

    try:
            
        fobj = open(fname, 'r')
        flag = False

        for line in fobj:
            words = line.split()
            
            for word in words:
                if (search_word == word):
                    Flag = True
                    print(f"Word - {search_word} is present in the file - {fname}.")
                    break

        if flag == False:
            print("word is not present")
        
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
Enter word you want to search : Shraddha
Word - Shraddha is present in the file - DemoFile.txt.

--------------------------------------------------------------------------------

Enter file name : DemoFile.txt
Enter word you want to search : Demo
word is not present

--------------------------------------------------------------------------------
"""