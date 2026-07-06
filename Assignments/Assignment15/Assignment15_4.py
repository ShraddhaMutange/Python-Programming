"""
Problem : Write a lambda funtion using reduce() which accepts a list of numbers and returns the addition of all numbers.
"""
from functools import reduce

Addition = lambda No1,No2 : No1 + No2

def main():
    size = int(input("Enter number of elements :"))
    Data = list()

    for i in range(size):
        print("Enter element", i+1, ":", end=" ")
        No = int(input())
        Data.append(No)

    print("Accepted Data :", Data)

    Ret = reduce(Addition, Data)
    print("Addition of all elements :", Ret)

if (__name__ == "__main__"):
    main()

"""
Output :

Enter number of elements :5
Enter element 1 : 10
Enter element 2 : 20
Enter element 3 : 30
Enter element 4 : 40
Enter element 5 : 50
Accepted Data : [10, 20, 30, 40, 50]
Addition of all elements : 150

"""
