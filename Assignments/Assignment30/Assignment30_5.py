"""
--------------------------------------------------------------------------------
Problem     :   Schedule a task taht executes every five minutes.
                The task should write the current date and time into a file named: Marvellous.txt
                New entries should be appended without removing previous entries.
Author      :   Shraddha Dhananjay Mutange
Date        :   25/07/2026
--------------------------------------------------------------------------------
"""
import datetime
import schedule
import time

def Display():
    fobj = open("Marvellous.txt", 'a')

    curr_datetime = str(datetime.datetime.now())

    fobj.write(f"Task executed at : {curr_datetime}\n")


def main():
    print("Automation script started")

    schedule.every(5).minutes.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(5)



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