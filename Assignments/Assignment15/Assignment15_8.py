"""
Problem : Write a lambda funtion using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.
"""

Divisibility = lambda No : ((No % 3 == 0) and (No % 5 == 0))

def main():
    size = int(input("Enter number of elements :"))
    Data = list()

    for i in range(size):
        print("Enter element", i+1, ":", end=" ")
        No = int(input())
        Data.append(No)

    print("Data before filter :", Data)

    FData = list(filter(Divisibility, Data))
    print("Data after filter :", FData)

if (__name__ == "__main__"):
    main()

"""
Output :

Enter number of elements :5
Enter element 1 : 3
Enter element 2 : 15
Enter element 3 : 12
Enter element 4 : 25
Enter element 5 : 30
Data before filter : [3, 15, 12, 25, 30]
Data after filter : [15, 30]

"""
