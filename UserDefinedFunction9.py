def BigBazar():
    print("Inside Big Bazar")

    def Amul():
        print("Inside Amul Ice-Cream Parlour")

    Amul()                  # Now this works
    Amul()

def main():
    BigBazar()              # Allowed
    

if __name__ == "__main__":
    main()