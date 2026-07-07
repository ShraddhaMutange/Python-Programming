"""
Problem : Create a module named as Arithmetic which nontains for functions Add() for addition, Sub() for subtraction, Mul() for multiplication and Div() for division. All functions accepts two numbers as parameters and perform the operation. Write one python program which calls all functions from Arithmetic module by accepting the parameters from the user.
"""

"""
----------------------------------------------------------------------------
------------------Import required modules-----------------------------------
----------------------------------------------------------------------------
"""
import Arithmetic as ar

"""
----------------------------------------------------------------------------
------------------Entry Point Function of the application-------------------
----------------------------------------------------------------------------
"""
def main():
    Value1 = int(input("Enter first Number : "))
    Value2 = int(input("Enter second Number : "))

    print(f"Addition is : {ar.Add(Value1,Value2)}")
    print(f"Substraction is : {ar.Sub(Value1,Value2)}")
    print(f"Multiplication is : {ar.Mul(Value1,Value2)}")
    print(f"Division is : {ar.Div(Value1,Value2)}")

if __name__ == "__main__":
    main()


"""
----------------------------------------------------------------------------
---------------------------------Output-------------------------------------
----------------------------------------------------------------------------

Enter first Number : 50
Enter second Number : 10
Addition is : 60
Substraction is : 40
Multiplication is : 500
Division is : 5.0

----------------------------------------------------------------------------
"""