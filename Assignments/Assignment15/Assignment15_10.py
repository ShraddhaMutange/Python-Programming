"""
Problem : Write a lambda funtion using filter() which accepts a list of numbers and returns the count of even numbers.
"""

CheckEven = lambda No : No % 2 == 0

def main():
    size = int(input("Enter number of elements :"))
    Data = list()

    for i in range(size):
        print("Enter element", i+1, ":", end=" ")
        No = int(input())
        Data.append(No)

    print("Data before filter :", Data)

    FData = list(filter(CheckEven, Data))
    print("Data after filter :", FData)

    print("\nTotal count of even numbers is :", len(FData))

if (__name__ == "__main__"):
    main()

"""
Output :

Enter number of elements :5
Enter element 1 : 1
Enter element 2 : 2
Enter element 3 : 3
Enter element 4 : 4
Enter element 5 : 5
Data before filter : [1, 2, 3, 4, 5]
Data after filter : [2, 4]

Total count of even numbers is : 2

"""
