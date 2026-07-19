class Demo:
    # Class variables
    Value1 = 10
    Value2 = 20

    # constructor (it is also instance methos)
    def __init__(self):
        # Instance variables
        self.No1 = 11
        self.No2 = 21

    # Instance method
    def Fun(self):
        print("Inside Instance method named as Fun")
        print(self.No1)
        print(self.No2)
        print(self.Value1)
        print(self.Value2)

dobj = Demo()
dobj.Fun()