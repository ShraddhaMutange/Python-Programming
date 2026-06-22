def Calculation(No1, No2):
    Sum = No1 + No2
    Diff = No1 - No2
    Prod = No1 * No2
    Div = No1 / No2

    return Sum,Diff,Prod,Div

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret1, Ret2, Ret3, Ret4 = Calculation(Value1, Value2)

    print("Addition is : ", Ret1)
    print("Substraction is : ", Ret2)
    print("Multiplication is : ", Ret3)
    print("Division is : ", Ret4)

if __name__ == "__main__":
    main()