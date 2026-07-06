"""
Problem : Write a lambda funtion using reduce() which accepts a list of numbers and returns the product of all elements.
"""
from functools import reduce

Product = lambda No1,No2 : No1 * No2

def main():
    size = int(input("Enter number of elements :"))
    Data = list()

    for i in range(size):
        print("Enter element", i+1, ":", end=" ")
        No = int(input())
        Data.append(No)

    print("Accepted Data :", Data)

    Ret = reduce(Product, Data)
    print("Product of all elements : ", Ret)

if (__name__ == "__main__"):
    main()

"""
Output :

Enter number of elements : 5
Enter element 1 : 1
Enter element 2 : 2
Enter element 3 : 3
Enter element 4 : 4
Enter element 5 : 5
Accepted Data : [1, 2, 3, 4, 5]
Product of all elements : 120

"""
