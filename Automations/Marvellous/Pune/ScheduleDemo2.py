import schedule
import time
import datetime

def Display():
    print("Jay Ganesh...")

def main():
    print("Automation script started")

    schedule.every(1).minute.do(Display)

    # Issue (ithe kahitari pahije process la alive thevnyasathi)

if __name__ == "__main__":
    main()