"""
Problem : Write a lambda function which accepts one number and returns True if number is even otherwise False.
"""

Even = lambda No : No % 2 == 0

def main():
    Value = int(input("Enter a number : "))

    Ret = Even(Value)
    if(Ret == True):
        print("Even number")
    else:
        print("Odd Number")


if (__name__ == "__main__"):
    main()

"""
Output :

Enter a number : 5
Odd Number

---------------------------------

Enter a number : 12
Even number

"""
