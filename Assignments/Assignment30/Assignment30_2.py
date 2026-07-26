"""
--------------------------------------------------------------------------------
Problem     :   Write a program that displays the current date and time after every one minute. Use datetime module.
Author      :   Shraddha Dhananjay Mutange
Date        :   25/07/2026
--------------------------------------------------------------------------------
"""
import datetime
import schedule
import time

def Display():
    print(f"Current date and time : {datetime.datetime.now()}")

def main():
    print("Automation script started")

    schedule.every(1).minute.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(2)



if (__name__ == "__main__"):
    main()

"""
--------------------------------------------------------------------------------
-----------------------------------Output---------------------------------------
--------------------------------------------------------------------------------

Automation script started
Current date and time : 2026-07-26 13:19:24.046207
Current date and time : 2026-07-26 13:20:24.052812
Current date and time : 2026-07-26 13:21:24.061696
Current date and time : 2026-07-26 13:22:24.068978
^CTraceback (most recent call last):
  File "/home/shraddha/Desktop/Python/Assignments/Assignment30/Assignment30_2.py", line 27, in <module>
    main()
  File "/home/shraddha/Desktop/Python/Assignments/Assignment30/Assignment30_2.py", line 22, in main
    time.sleep(2)
KeyboardInterrupt


--------------------------------------------------------------------------------
"""