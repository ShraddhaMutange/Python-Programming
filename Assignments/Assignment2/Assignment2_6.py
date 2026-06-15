# Problem : Write a program to accept two numbers from the user and prints their:
#           - Addition
#           - Subtraction
#           - Multiplication
#           - Division

def Addition(No1, No2):
    return No1 + No2

def Subtraction(No1, No2):
    return No1 - No2

def Multiplication(No1, No2):
    return No1 * No2

def Division(No1, No2):
    return No1 / No2

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    print("Addition is : ", Addition(No1, No2))
    print("Subtraction is : ", Subtraction(No1, No2))
    print("Multiplication is : ", Multiplication(No1, No2))
    print("Division is : ", Division(No1, No2))

if (__name__ == "__main__"):
    main()

# -----------------------------------------------------------------------
# ---------------------------------Output--------------------------------
# -----------------------------------------------------------------------
# 
# Enter first number : 
# 21
# Enter second number : 
# 11
# Addition is :  32
# Subtraction is :  10
# Multiplication is :  231
# Division is :  1.9090909090909092
# 
# -----------------------------------------------------------------------