import csv


print("""welcome to the library
      1) to add book
      2) to remove book (not availabe for now(only manual remove)) 
      3) to show all available books 
      4) to search and read specific book   
      5) to borrow (not available (only manual borrow))
      6) to return a book only if you borrowed (not available (only manual return))
      7) to exit library
      """)

print("""list of current available books
           """)
with open("presentation.csv", "r") as libry:
    books = csv.DictReader(libry)
    for items in books:
        print(items["books"])


print("""
      
      """)
while True:
    option = int(input("select a number>>>"))


    if option == 1:
        
        class parent:
            def __init__(self, name, author, content):
                self.name = name
                self.author = author
                self.content = content
                
            def show(self):
                o = open("presentation.csv", "a", newline="")
                o.write(self.name) and o.write(",") and o.write(self.author) and o.write(",") and o.write(self.content)
              
                print(f"{self.name} written by {self.author} has been added")


        class cat(parent):
            def speak(self):
                print("meow")

            
            
        name = input("book name>>")  
        author = input("book author>>") 
        content = input("write every thing here>>") 


        c = cat(name, author, content)
        c.show()

    # elif option == 2:
    #     class parent:
    #             def __init__(self, name, book,):
    #                 self.name = name
    #                 self.book = book
                    
    #             def show(self):
    #                 check = open("presentation.csv", "r")
    #                 if self.name in open("presentation.csv", "r"):
    #                     print("available")
    #                 #    write = open("presentation.csv", "w")
    #                 #    write.write("abc")
                    
                    
    #                 #    print(f"{self.name} has been removed")
    #                 #    print("""list of current available books after deleting
                                            
    #                                         # """)
    #                 #    with open("presentation.csv", "r") as file:
    #                 #         folder = csv.reader(file)
    #                 #         for items in folder:
    #                 #             print(items)
    #                 elif self.name not in open("presentation.csv", "r"):
    #                     print("not available")
        
        
    #     class cat(parent):
    #         def speak(self):
    #             print("meow")
    
    
            
    #     name = input("book name to be removed>>")  
    #     book = open("presentation.csv", "r")

        # c = cat(name, book)
        # c.show()
            
    elif option == 3:
        print("""all availables books
            
            """)
        with open("presentation.csv", "r") as folder:
            file = csv.DictReader(folder)
            for items in file:
                print(items["books"])
        
        
    elif option == 4:
        class parent:
            def __init__(self, name):
                self.name = name
              
            
            def show(self):
                with open("presentation.csv", "r") as file:
                    folder = csv.DictReader(file)
                    for items in folder:
                        if items["books"] == self.name:
                            print(f"""book name: {self.name}""")
                            print(items["content"])
                            print("""thanks for reading this book
                                  """)
                            input("press enter to continue..")
                      
                        
          



        class cat(parent):
            def speak(self):
                print("meow")

            
            
        name = input("book name FULL>>>")  


        c = cat(name)
        c.show()
        
        
    # elif option == 5:
    #     class parent:
    #         def __init__(self, name,  book, borrow):
    #             self.name = name
    #             self.book = book
    #             self.borrow = borrow
            
    #         def show(self):
    #             if self.name in book:
    #                 self.borrow.append(self.name)
    #                 self.book.remove(self.name)
    #                 for items in self.borrow:
    #                     print("below is list of borrowed books")
    #                     print(items)
                    
    #                     print("below are the list of available books")
    #                     print(book)
    #             elif self.name not in book:
    #                 print("book not available to be borrowed")
            



    #     class cat(parent):
    #         def speak(self):
    #             print("nothing unless error")

            
            
    #     name = input("book name to be borrowed>>")  


    #     c = cat(name,  book, borrowed)
    #     c.show()
            

        




    # elif option == 6:
    #     class parent:
    #         def __init__(self, name,  book, borrow):
    #             self.name = name
    #             self.book = book
    #             self.borrow = borrow
            
    #         def show(self):
    #             if self.name in self.borrow:
    #                 self.borrow.remove(self.name)
    #                 self.book.append(self.name)
    #                 for items in self.borrow:
    #                     print(f"below is list of your  borrowed books after you returned {self.borrow}")
    #                     print(items)
                    
    #                 print(f"below are the list of available books after you returned {self.name}")
    #                 print(book)
    #             elif self.name not in book:
    #                 print("book not available among borrowed collections")
            



        # class cat(parent):
        #     def speak(self):
        #         print("nothing unless error code")

            
            
        # name = input("book name to be returned>>")  


        # c = cat(name,  book, borrowed)
        # c.show()
            

        

    elif option == 2 or option == 5 or option == 6:
        print("ohhh, this feature is not avilable for now")
        
    elif option == 7:
        print("thanks for patronizing our library, we hope to see u next time..")
        exit()

   
    else:
        print("option input was not incline with what was to be inputed")
    


#completed 12:33 am, saturday











