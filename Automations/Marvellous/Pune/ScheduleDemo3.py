import schedule
import time
import datetime

def Display():
    print("Jay Ganesh...", datetime.datetime.now())

def main():
    print("Automation script started")

    schedule.every(1).minute.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)   # 1 second

    print("End of Automation Script")   # this line will never run, bc it is written after the loop which will run infinitely

if __name__ == "__main__":
    main()