"""
Author  : Shraddha Dhananjay Mutange
"""

"""
Problem : Write a lambda funtion using filter() which accepts a list of strings and returns the list of strings having length greater than 5.
"""

CheckLength = lambda word : len(word) > 5

def main():
    size = int(input("Enter number of words :"))
    Data = list()

    for i in range(size):
        print("Enter string", i+1, ":", end=" ")
        word = input()
        Data.append(word)

    print("Accepted Data :", Data)

    FData = list(filter(CheckLength, Data))
    print("Strings having length greater than 5 :", FData)

if (__name__ == "__main__"):
    main()

"""
Output :

Enter number of words :5
Enter string 1 : marvellous
Enter string 2 : shraddha
Enter string 3 : hi
Enter string 4 : hello
Enter string 5 : ganesh
Accepted Data : ['marvellous', 'shraddha', 'hi', 'hello', 'ganesh']
Strings having length greater than 5 : ['marvellous', 'shraddha', 'ganesh']

"""
