"""
Problem : Write a lambda function which accepts three numbers and returns the largest number.
"""

Maximum = lambda No1,No2,No3 : max(No1,No2,No3)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Value3 = int(input("Enter third number : "))

    Ret = Maximum(Value1, Value2, Value3)
    
    print("Maximum number is : ", Ret)
    


if (__name__ == "__main__"):
    main()

"""
Output :

Enter first number : 10
Enter second number : 11
Enter third number : 21
Maximum number is :  21

--------------------------------------------

Enter first number : 21
Enter second number : 51
Enter third number : 14
Maximum number is :  51

"""
