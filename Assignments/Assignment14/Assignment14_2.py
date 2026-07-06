"""
Problem : Write a lambda function which accepts one number and returns cube of that number.
"""

Cube = lambda No : No * No *No

def main():
    Value = int(input("Enter a number : "))

    Ret = Cube(Value)
    print("Cube of",Value,"is :", Ret)


if (__name__ == "__main__"):
    main()

"""
Output :

Enter a number : 2
Cube of 2 is : 8

"""
