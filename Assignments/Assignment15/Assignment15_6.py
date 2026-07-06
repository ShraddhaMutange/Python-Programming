"""
Problem : Write a lambda funtion using reduce() which accepts a list of numbers and returns the minimum element.
"""
from functools import reduce

Minimum = lambda No1,No2 : min(No1,No2)

def main():
    size = int(input("Enter number of elements :"))
    Data = list()

    for i in range(size):
        print("Enter element", i+1, ":", end=" ")
        No = int(input())
        Data.append(No)

    print("Accepted Data :", Data)

    Ret = reduce(Minimum, Data)
    print("Minimum element :", Ret)

if (__name__ == "__main__"):
    main()

"""
Output :

Enter number of elements :5
Enter element 1 : 81 
Enter element 2 : 18
Enter element 3 : 27
Enter element 4 : 72
Enter element 5 : 45
Accepted Data : [81, 18, 27, 72, 45]
Minimum element : 18

"""
