"""
Problem Description :   Write a program that accepts a directory name from the user and counts the numbers of files inside it every five minutes.
                        Write the result into: DirectoryCountLog.txt

                        Each entry should contain:
                        - Directory path
                        - Number of files
                        - Date and time
"""

import schedule
import time

def MondayMessage():
    print("Start your weekly goals")

def WednesdayMessage():
    print("Review your weekly progress")

def FridayMessage():
    print("Weekly work completed")

def main():

    schedule.every().monday.at("09:00").do(MondayMessage)
    schedule.every().wednesday.at("17:00").do(WednesdayMessage)
    schedule.every().friday.at("18:00").do(FridayMessage)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

