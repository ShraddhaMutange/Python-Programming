"""
--------------------------------------------------------------------------------
Problem     :   Write a script that performs a file backup every hour.
                The program should : 
                1. Access the source file path.
                2. Accept the destination directory path.
                3. Copy the source file to the destination directory.
                4. Add the current date and time to the backup filename.
                5. Write the backup operation details into: backup_log.txt
                Use shutil module for file copying.
Author      :   Shraddha Dhananjay Mutange
Date        :   25/07/2026
--------------------------------------------------------------------------------
"""

import shutil
import sys
import os
import time
import datetime

def Backup(src_path, dest_dir):
    Border = "-"*50
    
    if (os.path.exists(src_path) == False):
        print(f"Source path - {src_path} does not exist.")
        return

    if os.path.exists(dest_dir) == False:
        os.mkdir(dest_dir)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_file = "Backup_%s.log"%(timestamp)

    backup_file = os.path.join(dest_dir,backup_file)

    # fobj = open(backup_file, 'w')

    # fobj.write(Border+"\n")
    # fobj.write(f"Python Automation Script\n")
    # fobj.write(Border+"\n\n")

    # srcobj = open(src_path, 'r')

    # Buffer = srcobj.read(1024)

    # while(len(Buffer) > 0):
    #     fobj.write(Buffer)
    #     Buffer = srcobj.read(1024)

    # srcobj.close()

    # fobj.write(Border+"\n\n")

    shutil.copy2(src_path, backup_file)

def main():
    
    try:
        print("Automation script started")

        Backup(sys.argv[1], sys.argv[2])

    except IndexError as eobj:
        print("Error occured : ", eobj)
        
    except Exception as eobj:
        print("Error occured : ", eobj)






if (__name__ == "__main__"):
    main()

