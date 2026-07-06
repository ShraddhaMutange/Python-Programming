"""
Problem : Write a lambda function which accepts two numbers and returns maximum number.
"""

Maximum = lambda No1,No2 : No1 > No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Maximum(Value1, Value2)
    if(Ret == True):
        print("Maximum number is :", Value1)
    else:
        print("Maximum number is :", Value2)
    


if (__name__ == "__main__"):
    main()

"""
Output :

Enter first number : 5
Enter second number : 5
Maximum number is : 5

-----------------------------------

Enter first number : 11
Enter second number : 21
Maximum number is : 21

-----------------------------------

Enter first number : 10
Enter second number : 11
Maximum number is : 11

"""
