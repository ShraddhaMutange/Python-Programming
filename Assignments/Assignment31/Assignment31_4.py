"""
Problem Description :   Write a program that screates a new log file after every ten minutes.
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

def CreateLogFile(dir_path):

    if os.path.exists(dir_path) == False or os.path.isdir(dir_path) == False:
        os.mkdir(dir_path)
    
    
    filename = "MarvellousLog_%s.txt"%datetime.datetime.now().strftime("%d_%m_%Y_%H:%M:%S")
    filename = os.path.join(dir_path,filename)

    fobj = open(filename, 'w')

    fobj.write("Log file created successfully.\n")
    
    creation_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")
    fobj.write(f"Creation Time : {creation_time}")   
                

def main():
    dir_path = input("Enter directory path : ")
    
    # ScanDirectory(dir_path)

    schedule.every(5).seconds.do(CreateLogFile, dir_path)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

