# Author    : Shraddha Dhananjay Mutange
# Date      : 15/06/2026

# Problem : Write a program that accepts two numbers from the user and prints their:
#           - Addition
#           - Subtraction
#           - Multiplication
#           - Division

def Addition(No1, No2):
    return (No1 + No2)

def Subtraction(No1, No2):
    return (No1 - No2)

def Multiplication(No1, No2):
    return (No1 * No2)

def Division(No1, No2):
    return (No1 / No2)

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

# -------------------------------------------------------------
# -------------------------Output------------------------------
# -------------------------------------------------------------
# 
# Enter first number : 
# 10
# Enter second number : 
# 5
# Addition is :  15
# Subtraction is :  5
# Multiplication is :  50
# Division is :  2.0
#  
# -------------------------------------------------------------