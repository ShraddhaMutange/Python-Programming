Increament = lambda No : (No + 1)

CheckEven = lambda No : (No % 2 == 0)

def main():
    Data = [13,12,8,10,11,20]
    print("Input Data is : ", Data)

    # FData = filter(CheckEven, Data)     # Error

    FData = list(filter(CheckEven, Data))

    print ("Data after filter : ", FData)

    MData = list(map(Increament, FData))
    
    print ("Data after Map : ", MData)



if __name__ == "__main__":
    main()