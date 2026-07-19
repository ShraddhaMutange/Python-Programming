def CheckEven(No):
    if No % 2 == 0:
        return True
    else:
        return False

def main():
    Value = int(input("Enter a number : "))

    Ret = CheckEven(Value)
    
    if Ret == True:
        print(Value, "is Even")
    else:
        print(Value, "is Odd")

if __name__ == "__main__":
    main()