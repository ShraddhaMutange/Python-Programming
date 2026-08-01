"""
Problem Description :   Write a program that scans a specified directory every minute.
                        The task should display:
                        - Directory name
                        - Number of files
                        - Number of subdirectories
                        - Date and time of scanning

                        Use the os module.

                        Example output:
                        Directory Scanned: E:/Data
                        Total Files: 15
                        Total Subdirectories: 4
                        Scan Time: 25-07-2026 04:30:00 PM
"""

import schedule
import datetime
import time
import os

def ScanDirectory(dir_path):
    
    result = dict()
    Count = 0
    
    for FolderName, SubFolder, FileName in os.walk(dir_path):
        
        result['Directory Scanned'] = FolderName

        for fname in FileName:
            Count = Count + 1

        result['Total Files'] = Count

        for subf in SubFolder:
            Count = Count + 1

        result['Total Subdirectories'] = Count

        curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")

        result['Scan Time'] = curr_time

        for key, value in result.items():
            print(f"{key} : {value}")
                

def main():
    dir_path = input("Enter directory path : ")
    
    # ScanDirectory(dir_path)

    schedule.every(5).seconds.do(ScanDirectory, dir_path)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
Output:

Enter directory path : /home/shraddha/Desktop/Python/Assignments/Assignment30
Directory Scanned : /home/shraddha/Desktop/Python/Assignments/Assignment30
Total Files : 8
Total Subdirectories : 9
Scan Time : 2026-08-01 09:47:15 AM
Directory Scanned : /home/shraddha/Desktop/Python/Assignments/Assignment30/DestDir
Total Files : 10
Total Subdirectories : 10
Scan Time : 2026-08-01 09:47:20 AM
Directory Scanned : /home/shraddha/Desktop/Python/Assignments/Assignment30
Total Files : 8
Total Subdirectories : 9
Scan Time : 2026-08-01 09:47:25 AM
Directory Scanned : /home/shraddha/Desktop/Python/Assignments/Assignment30/DestDir
Total Files : 10
Total Subdirectories : 10
Scan Time : 2026-08-01 09:47:25 AM
^CTraceback (most recent call last):
  File "/home/shraddha/Desktop/Python/Assignments/Assignment31/Assignment31_3.py", line 62, in <module>
    main()
  File "/home/shraddha/Desktop/Python/Assignments/Assignment31/Assignment31_3.py", line 59, in main
    time.sleep(1)
KeyboardInterrupt


"""