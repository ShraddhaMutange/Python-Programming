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
