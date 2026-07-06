from functools import reduce

def Increament(No):
    return (No + 1)

def CheckEven(No):
    return (No % 2 == 0)

def Addition(No1, No2):
    return No1+No2
    

def main():
    Data = [13,12,8,10,11,20]
    print("Input Data is : ", Data)

    # FData = filter(CheckEven, Data)     # Error

    FData = list(filter(CheckEven, Data))

    print ("Data after filter : ", FData)

    MData = list(map(Increament, FData))
    
    print ("Data after Map : ", MData)

    RData = reduce(Addition, MData)
    print ("Data after Reduce : ", RData)


if __name__ == "__main__":
    main()