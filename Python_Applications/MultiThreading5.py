def SumEven(No):
    sum = 0

    for i in range(2, No, 2):
        sum = sum + i

    print("Summation of even :", sum)

def SumOdd(No):
    sum = 0

    for i in range(1, No, 2):
        sum = sum + i

    print("Summation of odd :", sum)
    
def main():
    # 2 + 4 + 6 + 8 = 20
    SumEven(10000000)
    # 1 + 3 + 5 + 7 + 9 = 25
    SumOdd(10)


if (__name__ == "__main__"):
    main()