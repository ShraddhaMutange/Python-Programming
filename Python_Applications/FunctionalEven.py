# Hybrid Application

# Functional Programming
CheckEven = lambda No : No % 2 == 0

# Procedural Programming
def main():
    Value = int(input("Enter a number : "))

    Ret = CheckEven(Value)      # Ret = (Value % 2 == 0)
    
    if Ret == True:
        print(Value, "is Even")
    else:
        print(Value, "is Odd")

if __name__ == "__main__":
    main()

