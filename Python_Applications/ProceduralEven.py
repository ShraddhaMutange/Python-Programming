def CheckEven(No):
    if No % 2 == 0:
        print(No, "is Even")
    else:
        print(No, "is Odd")

def main():
    Value = int(input("Enter a number : "))

    CheckEven(Value)
    

if __name__ == "__main__":
    main()