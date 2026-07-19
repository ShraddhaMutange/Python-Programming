"""
---------------------------------------------------------------------------------------------------------------------
Problem :   Write a Python program to implement a class named Numbers with the following specifications:
            - The class should contain one instance variable:
                - Value
            - Define a constructor (__init__) that accepts a number from user and initializes Value.
            - Implement an instance method:
                - CheckPrime() - returns True if the number is prime, otherwise returns False.
                - CheckPerfect() - returns True if the number is perfect, otherwise returns False.
                - Factors() - displays all factors of the number 
                - SumFactors() - returns the sum of all factors
            - Create multiple objects and call all methods
---------------------------------------------------------------------------------------------------------------------
"""

class Numbers:
    def __init__(self,A):
        self.Value = A

    def CheckPrime(self):
        No = self.Value
        Flag = True

        for i in range(2,(No//2)+1):
            if (No % i == 0):
                Flag = False
                break
        
        return Flag
    
    def CheckPerfect(self):
        No = self.Value
        Sum = 0

        for i in range(1,(No//2)+1):
            if (No % i == 0):
                Sum = Sum + i
        
        return (No == Sum)

    def Factors(self):
        No = self.Value

        for i in range(1,(No//2)+1):
            if (No % i == 0):
                print(f"{i}\t")
        
    def SumFactors(self):
        No = self.Value
        Sum = 0

        for i in range(1,(No//2)+1):
            if (No % i == 0):
                Sum = Sum + i
        
        return Sum

def main():
    print("Enter a number : ")
    Value = int(input())

    Nobj = Numbers(Value)

    Ret = Nobj.CheckPrime()
    if (Ret == True):
        print(f"{Value} is Prime Number")
    else:
        print(f"{Value} is Not a Prime Number")

    Ret = Nobj.CheckPerfect()
    if (Ret == True):
        print(f"{Value} is Perfect Number")
    else:
        print(f"{Value} is Not a Perfect Number")

    Nobj.Factors()

    Ret = Nobj.SumFactors()
    print(f"Sum of all factors of {Value} is : {Ret}")

if __name__ == "__main__":
    main()


"""
--------------------------------------------------------------------------------------
----------------------------------------Output----------------------------------------
--------------------------------------------------------------------------------------

Enter a number : 
6
6 is Not a Prime Number
6 is Perfect Number
1	
2	
3	
Sum of all factors of 6 is : 6

--------------------------------------------------------------------------------------

Enter a number : 
100
100 is Not a Prime Number
100 is Not a Perfect Number
1	
2	
4	
5	
10	
20	
25	
50	
Sum of all factors of 100 is : 117

--------------------------------------------------------------------------------------
"""