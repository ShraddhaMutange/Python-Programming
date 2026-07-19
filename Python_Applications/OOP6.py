class Demo:
    # Class variables
    Value1 = 10
    Value2 = 20

    # constructor (it is also instance method)
    def __init__(self):
        # Instance variables
        self.No1 = 11
        self.No2 = 21

obj1 = Demo()
obj2 = Demo()

obj1.No1 = 0

print(obj1.No1) # 0
print(obj2.No1) # 11

Demo.Value1 = 0

print(Demo.Value1)
