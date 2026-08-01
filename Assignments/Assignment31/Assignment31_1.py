"""
Problem Description :   Write a program that accepts:
                        - A message from the user
                        - A time interval in seconds
                        Schedule the program to display the message repeatedly after the specified interval.

                        example input:
                        Enter message: Jay Ganesh
                        Enter interval in 5 seconds: 5

                        expected output:
                        Jay Ganesh
                        every five seconds.

                        Validate that the interval is greater than zero.
"""

import schedule
import time

def DisplayMessage(msg):
    print(msg)

def main():
    msg = input("Enter message : ")
    time_interval = int(input("Enter interval in seconds : "))

    if (time_interval <= 0):
        print("Please enter valid time interval.")
        print("Hint : interval must be greater than zero")
        return
    
    schedule.every(time_interval).seconds.do(DisplayMessage, msg)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


"""
Output:

Enter message : Jay Ganesh...
Enter interval in seconds : 2
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