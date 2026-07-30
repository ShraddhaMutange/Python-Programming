"""
--------------------------------------------------------------------------------
Problem     :   Write a script that performs a file backup every hour.
                
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

