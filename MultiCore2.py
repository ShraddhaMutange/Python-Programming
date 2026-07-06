def SumCube(No):
    sum = 0

    for i in range(1, No+1):
        sum = sum + (i ** 3)    # i ** 3 => i to the power 3

    return sum

def main():
    Value = int(input("Enter a number : "))
    Ret = SumCube(Value)
    print("Result is :", Ret)

if (__name__ == "__main__"):
    main()