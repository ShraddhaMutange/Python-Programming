"""
Problem : Write a lambda function which accepts one number and returns True if number is even otherwise False.
"""

Odd = lambda No : No % 2 == 1

def main():
    Value = int(input("Enter a number : "))

    Ret = Odd(Value)
    if(Ret == True):
        print("Odd number")
    else:
        print("Even Number")


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
