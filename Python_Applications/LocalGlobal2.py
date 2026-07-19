no = 11     # Global Variable

def Display():
    a = 21  # Local Variable
    print("From Display : ", no)
    print("From Display value of a is : ", a)
    

def Demo():
    print("From Demo : ", no)
    print("From Demo value of a is : ", a)      # NameError: name 'a' is not defined

Display()
Demo()