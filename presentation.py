# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author


# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def display_books(self):
#         for book in self.books:
#             print(f"{book.title} by {book.author}")


# # Adding books to the library
# library = Library()

# library.add_book(Book("1984", "George Orwell"))
# library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

# library.display_books()




# class library:
#     def __init__(self, name, author):
#         self.name = name
#         self.authoe = author
        
# class book(library):
    
#     def __init__(self):
#         self.all_books = ["me"]
        
#     def appending(self):
#         self.all_books.append(self.name)
        
#     def display(self):
#         for items in self.all_books:
#             print(items)
#         # print(self.appending)

# libra = library("mary and the lamb", "ette mary")
# boo = book()
# boo.display()













# class parent:
#     def __init__(self, name, author, book):
#         self.name = name
#         self.author = author
#         self.book = book
        
#     def show(self):
#         self.book.append(self.name + " by " + self.author)
        
#         for items in self.book:
#             print(items)
#         print(f"{self.name} written by {self.author} has been added")


# class cat(parent):
#     def speak(self):
#         print("meow")

    
# book = []
    
# name = input("book name>>")  
# author = input("book author>>")  


# c = cat(name, author, book)
# c.show()









print("""welcome to the library
      1) to add book
      2) to remove book  
      3) to show all available books 
      4) to search a book   
      5) to borrow
      6) to return a book only if you borrowed
      7) to exit library
      """)



book = ["fidelis the webdev", "uzor the shoe maker", "let me die alone", "lion and jewel", "rich dad poordad", "tears of joy"]
borrowed = []

while True:
    option = int(input("select a number>>>"))


    if option == 1:
        
        class parent:
            def __init__(self, name, author, book,):
                self.name = name
                self.author = author
                self.book = book
                
            def show(self):
                self.book.append(self.name + " by " + self.author)
                

                print(f"{self.name} written by {self.author} has been added")


        class cat(parent):
            def speak(self):
                print("meow")

            
            
        name = input("book name>>")  
        author = input("book author>>")  


        c = cat(name, author, book)
        c.show()

    elif option == 2:
        class parent:
                def __init__(self, name, book,):
                    self.name = name
                    self.book = book
                    
                def show(self):
                    self.book.remove(self.name)
                    
                    
                    print(f"{self.name} has been removed")
                    print("""list of current available books after deleting
                                        
                                        """)
                    for items in self.book:
                        print(items)
        
        
        class cat(parent):
            def speak(self):
                print("meow")
    
    
            
        name = input("book name>>")  


        c = cat(name, book)
        c.show()
            
    elif option == 3:
        print("""all availables books
            
            """)
        for items in book:
         print(items)
        
        
    elif option == 4:
        class parent:
            def __init__(self, name,  book):
                self.name = name
                self.book = book
            
            def show(self):
                # self.book.find(self.name)
                if self.name in book:
                    print(f"{self.name} is available")
                elif self.name not in book:
                    print(f"{self.name} was not found..")
                



        class cat(parent):
            def speak(self):
                print("meow")

            
            
        name = input("book name or authors name to search>>")  


        c = cat(name,  book)
        c.show()
        
        
    elif option == 5:
        class parent:
            def __init__(self, name,  book, borrow):
                self.name = name
                self.book = book
                self.borrow = borrow
            
            def show(self):
                if self.name in book:
                    self.borrow.append(self.name)
                    self.book.remove(self.name)
                    for items in self.borrow:
                        print("below is list of borrowed books")
                        print(items)
                    
                        print("below are the list of available books")
                        print(book)
                elif self.name not in book:
                    print("book not available to be borrowed")
            



        class cat(parent):
            def speak(self):
                print("nothing unless error")

            
            
        name = input("book name to be borrowed>>")  


        c = cat(name,  book, borrowed)
        c.show()
            

        




    elif option == 6:
        class parent:
            def __init__(self, name,  book, borrow):
                self.name = name
                self.book = book
                self.borrow = borrow
            
            def show(self):
                if self.name in self.borrow:
                    self.borrow.remove(self.name)
                    self.book.append(self.name)
                    for items in self.borrow:
                        print(f"below is list of your  borrowed books after you returned {self.borrow}")
                        print(items)
                    
                    print(f"below are the list of available books after you returned {self.name}")
                    print(book)
                elif self.name not in book:
                    print("book not available among borrowed collections")
            



        class cat(parent):
            def speak(self):
                print("nothing unless error code")

            
            
        name = input("book name to be returned>>")  


        c = cat(name,  book, borrowed)
        c.show()
            

        

    elif option == 7:
        print("thanks for patronizing our library, we hope to see u next time..")
        exit()

   
    else:
        print("option input was not incline with what was to be inputed")
    


#completed 12:33 am, saturday











