"""
Problem Description :   Write a Python program that monitors the size of a specified file every 30 seconds.
                        Write the following details into: FileSizeLog.txt
                        - File path
                        - File size in bytes
                        - Date and time
                        Handle the situation where the file does not exist.
"""

import schedule
import datetime
import time
import os
from pathlib import Path


def MonitorFileSize(file_to_monitor, log_filename = "FileSizeLog.txt"):

    if os.path.exists(file_to_monitor) == False:
        print("File does not exist in specified path")
        print("Please enter valid filename")
        return
    
    fobj = open(log_filename, 'a')

    fobj.write(f"\nFile path: {Path.cwd()}\n")
    fobj.write(f"File size: {os.path.getsize(file_to_monitor)}\n")
    fobj.write(f"Date and time: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")}\n")


                   
         
def main():
    fname = input("Enter file name to monitor size : ")

    schedule.every(10).seconds.do(MonitorFileSize, fname)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

