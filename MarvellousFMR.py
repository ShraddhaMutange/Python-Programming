from functools import reduce

Increament = lambda No : (No + 1)

CheckEven = lambda No : (No % 2 == 0)

Addition = lambda No1, No2 : No1+No2

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        
        if(Ret == True):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task, Elements):
    Result = 0
    
    for no in Elements:
        Result = Task(Result, no)

    return Result

"""
def reduceX(Task, Elements):
    Result = Elements[0]
    
    for i in range(1,len(Elements)):
        Result = Task(Result, Elements[i])

    return Result
"""
    

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
    