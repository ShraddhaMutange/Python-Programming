"""
---------------------------------------------------------------------------------------------------------------------
Problem :   Write a Python program to implement a class named Arithmetic with the following characteristics:
            - The class should contain two instance variable : Value1 and Value2.
            - Define a constructor (__init__) that initializes all instance variables to 0.
            - Implement the following instance methods:
                - Accept() - accepts values for Value1 and Value2 from user.
                - Addition() - returns the addition of Value1 and Value2.
                - Substraction() - returns the substraction of Value1 and Value2.
                - Multiplication() - returns the multiplication of Value1 and Value2.
                - Division() - returns the division of Value1 and Value2. (Handle division by zero properly)
            - Create multiple objects of the Arithematic class and invoke all the instance methods.
---------------------------------------------------------------------------------------------------------------------
"""

class Arithematic:
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter first number : ")
        self.Value1 = int(input())

        print("Enter second number : ")
        self.Value2 = int(input())

    def Addition(self):
        Sum = 0
        Sum = self.Value1 + self.Value2
        return Sum
    
    def Substraction(self):
        Sub = 0
        Sub = self.Value1 - self.Value2
        return Sub
    
    def Multiplication(self):
        Mul = 0
        Mul = self.Value1 * self.Value2
        return Mul
    
    def Division(self):
        Div = 0

        try:
            Div = self.Value1 / self.Value2
        except ZeroDivisionError as zobj:
            print("Error occured : ", zobj)

        return Div
    
Aobj1 = Arithematic()

Aobj1.Accept()

Ret = Aobj1.Addition()
print("Addition is : ", Ret)

Ret = Aobj1.Substraction()
print("Substraction is : ", Ret)

Ret = Aobj1.Multiplication()
print("Multiplication is : ", Ret)

Ret = Aobj1.Division()
print("Division is : ", Ret)
    

    



"""
--------------------------------------------------------------------------------------
----------------------------------------Output----------------------------------------
--------------------------------------------------------------------------------------

Enter first number : 
12
Enter second number : 
4
Addition is :  16
Substraction is :  8
Multiplication is :  48
Division is :  3.0

--------------------------------------------------------------------------------------

Enter first number : 
12
Enter second number : 
12
Addition is :  24
Substraction is :  0
Multiplication is :  144
Division is :  1.0

--------------------------------------------------------------------------------------

Enter first number : 
12
Enter second number : 
0
Addition is :  12
Substraction is :  12
Multiplication is :  0
Error occured :  division by zero
Division is :  0

--------------------------------------------------------------------------------------
"""