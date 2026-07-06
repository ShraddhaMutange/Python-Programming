"""
Problem : Write a lambda funtion using reduce() which accepts a list of numbers and returns the maximum element.
"""
from functools import reduce

Maximum = lambda No1,No2 : max(No1,No2)

def main():
    size = int(input("Enter number of elements :"))
    Data = list()

    for i in range(size):
        print("Enter element", i+1, ":", end=" ")
        No = int(input())
        Data.append(No)

    print("Accepted Data :", Data)

    Ret = reduce(Maximum, Data)
    print("Maximum element :", Ret)

if (__name__ == "__main__"):
    main()

"""
Output :

Enter number of elements :5
Enter element 1 : 98
Enter element 2 : 101
Enter element 3 : 151
Enter element 4 : 63
Enter element 5 : 45
Accepted Data : [98, 101, 151, 63, 45]
Maximum element : 151

"""
