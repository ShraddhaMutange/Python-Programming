print("-------------------------------------------")
print("----------Ticket Pricing Software----------")
print("-------------------------------------------")

print("Please enter your age : ")
Age = int(input())

if (Age > 0 and Age <= 5):
    print("Free Entry")
elif (Age > 5 and Age <= 18):
    print("Ticket price for you : 900")
elif (Age > 18 and Age <= 40):
    print("Ticket price for you : 1200")
else:
    print("Ticket price for you : 500")
