"""
--------------------------------------------------------------------------------
Problem     :   Write a script that schedules the following tasks:
                - Print Lunch Time! every day at 1:00 PM
                - Print "Wrap up work" every day at 6:00 PM.
                Both taska should be handled by separate functions.
Author      :   Shraddha Dhananjay Mutange
Date        :   25/07/2026
--------------------------------------------------------------------------------
"""

import schedule
import time

def DisplayLunch():
    print(f"Lunch Time!")

def DisplayWrap():
    print(f"Wrap up work")


def main():
    print("Automation script started")

    schedule.every().day.at("13:00").do(DisplayLunch)
    schedule.every().day.at("18:00").do(DisplayLunch)

    while(True):
        schedule.run_pending()
        time.sleep(1)



if (__name__ == "__main__"):
    main()

