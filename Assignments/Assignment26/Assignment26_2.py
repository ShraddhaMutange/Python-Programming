"""
---------------------------------------------------------------------------------------------------------------------
Problem :   Write a Python program to implement a class named Circle with the following specifications:
            - The class should contain three instance variable : Radius, Area and Circumference.
            - The class should contain one class variable named PI, initialized to 3.14.
            - Define a constructor (__init__) that initializes all instance variables to 0.0.
            - Implement the following instance methods:
                - Accept() - accepts the radius of the circle from the user.
                - CalculateArea() - calculates the area of the circle and stores it in the Area variable.
                - CalculateCircumference() - calculate circumference of the circle and stores it in the Circumference variable.
                - Display() - displays the values of Radius, Area, and Circumference.
            - Create multiple objects of the Circle class and invoke all the instance methods for each object.
---------------------------------------------------------------------------------------------------------------------
"""

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter radius : ")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius : {self.Radius}")
        print(f"Area : {self.Area}")
        print(f"Circumference : {self.Circumference}")

cobj1 = Circle()

cobj1.Accept()
cobj1.CalculateArea()
cobj1.CalculateCircumference()
cobj1.Display()



"""
--------------------------------------------------------------------------------------
----------------------------------------Output----------------------------------------
--------------------------------------------------------------------------------------

Enter radius : 
2
Radius : 2.0
Area : 12.56
Circumference : 12.56

--------------------------------------------------------------------------------------
"""