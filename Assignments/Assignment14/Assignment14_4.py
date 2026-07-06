"""
Problem : Write a lambda function which accepts two numbers and returns minimum number.
"""

Minimum = lambda No1,No2 : No1 < No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Minimum(Value1, Value2)
    if(Ret == True):
        print("Minimum number is :", Value1)
    else:
        print("Minimum number is :", Value2)
    


if (__name__ == "__main__"):
    main()

"""
Output :

Enter first number : 11
Enter second number : 21
Minimum number is : 11

---------------------------------------------

Enter first number : 10
Enter second number : 11
Minimum number is : 10

---------------------------------------------

Enter first number : 5
Enter second number : 5
Minimum number is : 5

"""
