"""
Problem Description :   Write a program that screates a new text file every minute.
                        The filename should contain the current date and time.

                        Example:
                        MarvellousLog_25_07_2026_16_30_00.txt

                        The file should contain:
                        Log file created successfully.
                        Creation Time: 25-07-2026 04:30:00 PM
"""

import schedule
import datetime
import time
import os


def CreateLogFile():

    os.mkdir("BackupDir")    
    
    filename = "File_%s.txt"%datetime.datetime.now().strftime("%d_%m_%Y_%H:%M:%S")
    filename = os.path.join("BackupDir",filename)

    fobj = open(filename, 'w')
    
    creation_date = datetime.datetime.now().strftime("%d-%m-%Y")
    creation_time = datetime.datetime.now().strftime("%H:%M:%S")
        
    fobj.write(f"File Name : {filename}\n")
    fobj.write(f"Creation Date : {creation_date}\n")
    fobj.write(f"Creation Time : {creation_time}\n")   
                   
         
def main():
    dir_path = input("Enter directory path : ")

    schedule.every(1).minute.do(CreateLogFile)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

