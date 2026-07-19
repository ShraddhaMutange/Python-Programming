from MarvellousLibrary import filterX, mapX, reduceX

Increament = lambda No : (No + 1)

CheckEven = lambda No : (No % 2 == 0)

Addition = lambda No1, No2 : No1+No2

    

def main():
    Data = [13,12,8,10,11,20]
    print("Input Data is : ", Data)

    # FData = filter(CheckEven, Data)     # Error

    FData = list(filterX(CheckEven, Data))

    print ("Data after filter : ", FData)

    MData = list(mapX(Increament, FData))
    
    print ("Data after Map : ", MData)

    RData = reduceX(Addition, MData)

    print ("Data after Reduce : ", RData)
    

if __name__ == "__main__":
    main()
    