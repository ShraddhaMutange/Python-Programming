def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Addition(Value1, Value2)

    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()

# code working flow : line 17 -> 18 -> 6,7,8,10,11,13, -> 1,2,3,4, -> 13,15, -> 18
