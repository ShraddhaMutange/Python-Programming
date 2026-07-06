"""
Problem : Write a lambda function which accepts one number and returns square of that number.
"""

Square = lambda No : No * No

def main():
    Value = int(input("Enter a number : "))

    Ret = Square(Value)
    print("Square of",Value,"is :", Ret)


if (__name__ == "__main__"):
    main()

"""
Output :

Enter a number : -8
Square of -8 is : 64

Enter a number : 15
Square of 15 is : 225

"""
