# python3 PlatformSurveillance_CommandLine.py 2 MarvellousLog
# python3 PlatformSurveillance_CommandLine.py time_interval FolderName
#               0                   1           2
# len(sys.argv) -> 3

# python3 PlatformSurveillance_CommandLine.py --h
# python3 PlatformSurveillance_CommandLine.py --u
#               0                 1
# len(sys.argv) -> 2

import psutil   # third party module
import sys
import os

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

    elif (len(sys.argv) == 3):
        pass

    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as arguments are not matching.")
        print("Please use --h or --u flag for getting more details.")

    print(Border)
    print("\tThank you for using our Automation System")
    print(Border)

if (__name__ == "__main__"):
    main()