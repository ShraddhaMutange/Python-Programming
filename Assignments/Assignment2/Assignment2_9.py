# Author    : Shraddha Dhananjay Mutange
# Date      : 15/06/2026

# Problem : Write a program that accepts user's name and age and displays:
#           Hello <name>, you will turn <age+1> next year.

def main():
    print("Enter your name : ")
    Name = input()

    print("Enter your age : ")
    Age = int(input())

    print("Hello", Name + ", you will turn", Age+1, "next year.")

if (__name__ == "__main__"):
    main()

# -------------------------------------------------------------
# -------------------------Output------------------------------
# -------------------------------------------------------------
# 
# Enter your name : 
# Shraddha
# Enter your age : 
# 20
# Hello Shraddha, you will turn 21 next year.
#  
# -------------------------------------------------------------