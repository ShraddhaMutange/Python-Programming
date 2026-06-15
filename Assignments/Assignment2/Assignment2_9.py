# Problem : Write a program to take user's name and age and display:
#           Hello <name>, you will turn <age+1> next year.

def main():
    print("Enter your name : ")
    Name = input()

    print("Enter your age (in years): ")
    Age = int(input())

    print("Hello", Name, "you will turn", Age+1, "next year.")

if (__name__ == "__main__"):
    main()

# -----------------------------------------------------------------------
# ---------------------------------Output--------------------------------
# -----------------------------------------------------------------------
# 
# Enter your name : 
# Shraddha
# Enter your age (in years): 
# 20
# Hello Shraddha you will turn 21 next year.
# 
# -----------------------------------------------------------------------