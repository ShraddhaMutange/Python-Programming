"""
Problem : Write a lambda funtion using map() which accepts a list of numbers and returns a list of squares of each number.
"""

Square = lambda No : No * No

def main():
    size = int(input("Enter number of elements :"))
    Data = list()

    for i in range(size):
        print("Enter element", i+1, ":", end=" ")
        No = int(input())
        Data.append(No)

    print("Data before map :", Data)

    MData = list(map(Square, Data))
    print("Data after map :", MData)

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
Data before map : [1, 2, 3, 4, 5]
Data after map : [1, 4, 9, 16, 25]

"""
