def BigBazar():
    print("Inside Big Bazar")

    def Amul():
        print("Inside Amul Ice-Cream Parlour")

def main():
    BigBazar()              # Allowed
    Amul()                  # Error : NameError
    BigBazar().Amul()       # Error : AttributeError

if __name__ == "__main__":
    main()