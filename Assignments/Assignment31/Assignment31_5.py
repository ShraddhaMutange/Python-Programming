"""
Problem Description :   Write a program that accepts a directory name from the user and counts the numbers of files inside it every five minutes.
                        Write the result into: DirectoryCountLog.txt

                        Each entry should contain:
                        - Directory path
                        - Number of files
                        - Date and time
"""

import schedule
import datetime
import time
import os

def CountFiles(dir_path):

    if (os.path.exists(dir_path) == False):
        print("Invalid path")
        return
    
    if (os.path.isdir(dir_path) == False):
        print("It is not a directory")
        return

    fobj = open("DirectoryCountLog.txt", 'w')

    Count = 0
    
    for FolderName, SubFolder, FileName in os.walk(dir_path):
        fobj.write(f"\nDirectory Path : {dir_path}\n")
        fobj.write(f"Directory Name : {FolderName}\n")
        
        for fname in FileName:
            Count = Count + 1

        fobj.write(f"Number of files : {Count}\n")
        fobj.write(f"Date and time : {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")}\n")

    fobj.close()       

                

def main():
    dir_path = input("Enter directory path : ")
    
    # CountFiles(dir_path)

    schedule.every(5).seconds.do(CountFiles, dir_path)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

