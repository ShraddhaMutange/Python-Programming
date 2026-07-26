"""
--------------------------------------------------------------------------------
Problem     :   Create a task that executes everyday at 9.00 AM and prints: 
                Namaskar...
                use : schedule.every().day.at("09.00").do(...)
Author      :   Shraddha Dhananjay Mutange
Date        :   25/07/2026
--------------------------------------------------------------------------------
"""
import datetime
import schedule
import time

def Display():
    print("Namaskar...", datetime.datetime.now())

def main():
    print("Automation script started")

    schedule.every().day.at("09:00").do(Display)

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
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...
^CTraceback (most recent call last):
  File "/home/shraddha/Desktop/Python/Assignments/Assignment30/Assignment30_1.py", line 27, in <module>
    main()
  File "/home/shraddha/Desktop/Python/Assignments/Assignment30/Assignment30_1.py", line 22, in main
    schedule.run_pending()
  File "/usr/local/lib/python3.12/dist-packages/schedule/__init__.py", line 854, in run_pending
    default_scheduler.run_pending()
  File "/usr/local/lib/python3.12/dist-packages/schedule/__init__.py", line 100, in run_pending
    for job in sorted(runnable_jobs):
               ^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

--------------------------------------------------------------------------------
"""