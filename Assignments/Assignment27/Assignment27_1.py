"""
---------------------------------------------------------------------------------------------------------------------
Problem :   Write a Python program to implement a class named BookStore with the following specifications:
            - The class should contain two instance variables:
                - Name (Book name)
                - Author (Book author)
            - The class should contain one class variable:
                - NoOfBooks (initialize it to 0)
            - Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
            - Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
            - Implement an instance method:
                - Display() should display book details in format :
                    <BookName> by <Author>. No. of Books: <NoOfBooks>
---------------------------------------------------------------------------------------------------------------------
"""

class BookStore:
    NoOfBooks = 0

    def __init__(self, A, B):
        self.BookName = A
        self.Author = B

        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.BookName} by {self.Author}. No. of Books: {BookStore.NoOfBooks}")

Bobj1 = BookStore("Linux System Programming", "Robert Love")
Bobj1.Display()

Bobj2 = BookStore("C Programming", "Dennis Ritchie")
Bobj2.Display()


"""
--------------------------------------------------------------------------------------
----------------------------------------Output----------------------------------------
--------------------------------------------------------------------------------------

Linux System Programming by Robert Love. No. of Books: 1
C Programming by Dennis Ritchie. No. of Books: 2

--------------------------------------------------------------------------------------
"""