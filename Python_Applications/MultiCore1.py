def SumCube(No):
    sum = 0

    for i in range(1, No+1):
        sum = sum + (i * i * i)

    return sum

def main():
    Value = int(input("Enter a number : "))
    Ret = SumCube(Value)
    print("Result is :", Ret)

if (__name__ == "__main__"):
    main()