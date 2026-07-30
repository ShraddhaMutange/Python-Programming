import psutil   # third party module
import sys
import os
import time
import schedule

def PlatformSurveillance(FolderName):
    Border = "-"*60

    Ret = False

    Ret = os.path.exists(FolderName)

    if (Ret == True):
        Ret = os.path.isdir(FolderName)

        if (Ret == False):
            print(f"Unable to proceed as directory name is existing but it is not a directory.")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory for the logfile gets created successfully")

    timstamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timstamp)
        
    fobj = open(FileName, 'w')

    print(f"Log file gets successfully created with name - {FileName}")


def main():
    Border = "-"*60
    print(Border)
    print("\tMarvellous Platform Surveillance System")
    print(Border)
    
    # --h & --u handling
    if (len(sys.argv) == 2):

        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform : ")
            print("1 : It fetches the information of running processes")
            print("2 : It fetches information about the primary storage as RAM")
            print("3 : It fetches information about the secondary storage as HDD")
            print("4 : It fetches the information about the microprocessor")
            print("5 : It gets auto-scheduled periodically")
            print("6 : It maintains all records into log file")
            print("7 : It sends the log files through mail periodically")


        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python3 {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for log file creation")

        else:
            print("Unable to proceed as arguments are not matching.")
            print("Please use --h or --u flag for getting more details.")

    # Actual project code
    elif (len(sys.argv) == 3):
        # PlatformSurveillance(sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurveillance, sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as arguments are not matching.")
        print("Please use --h or --u flag for getting more details.")

    print(Border)
    print("\tThank you for using our Automation System")
    print(Border)

if (__name__ == "__main__"):
    main()