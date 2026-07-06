def CheckEven(No):
    return No % 2 == 0

def main():
    Value = int(input("Enter a number : "))

    Ret = CheckEven(Value)
    
    if Ret == True:
        print(Value, "is Even")
    else:
        print(Value, "is Odd")

if __name__ == "__main__":
    main()

