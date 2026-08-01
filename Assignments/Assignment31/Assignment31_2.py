"""
Problem Description :   Create a function named:
                        DisplayMessage(message)

                        Schedule the function using:
                        schedule.every(5).seconds.do(DisplayMessage, message)

                        The message should be accepted from the user.
"""

import schedule
import time

def DisplayMessage(msg):
    print(msg)

def main():
    msg = input("Enter message : ")
    
    schedule.every(5).seconds.do(DisplayMessage, msg)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
Output:

Enter message : Jay Ganesh...
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...
Jay Ganesh...
^CTraceback (most recent call last):
  File "/home/shraddha/Desktop/Python/Assignments/Assignment31/Assignment31_1.py", line 40, in <module>
    main()
  File "/home/shraddha/Desktop/Python/Assignments/Assignment31/Assignment31_1.py", line 37, in main
    time.sleep(1)
KeyboardInterrupt

"""