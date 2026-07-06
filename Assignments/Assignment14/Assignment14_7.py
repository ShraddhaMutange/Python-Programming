"""
Problem : Write a lambda function which accepts one number and returns True if number is even otherwise False.
"""

DivBy5 = lambda No : No % 5 == 0

def main():
    Value = int(input("Enter a number : "))

    Ret = DivBy5(Value)
    if(Ret == True):
        print("Divisible by 5")
    else:
        print("Not divisible by 5")


if (__name__ == "__main__"):
    main()

"""
Output :

Enter a number : 15
Divisible by 5

-----------------------------------------

Enter a number : 14
Not divisible by 5

"""
