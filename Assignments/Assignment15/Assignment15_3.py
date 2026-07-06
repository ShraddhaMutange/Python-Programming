"""
Problem : Write a lambda funtion using filter() which accepts a list of numbers and returns a list of odd numbers.
"""

Odd = lambda No : No % 2 == 1

def main():
    size = int(input("Enter number of elements :"))
    Data = list()

    for i in range(size):
        print("Enter element", i+1, ":", end=" ")
        No = int(input())
        Data.append(No)

    print("Data before filter :", Data)

    FData = list(filter(Odd, Data))
    print("Data after filter :", FData)

if (__name__ == "__main__"):
    main()

"""
Output :

Enter number of elements :5
Enter element 1 : 10
Enter element 2 : 11
Enter element 3 : 12
Enter element 4 : 13
Enter element 5 : 14
Data before filter : [10, 11, 12, 13, 14]
Data after filter : [11, 13]

"""
