class Book:
    def __init__(self,title,author,publication_year):
           self.title=title
           self.author=author
           self.publication_year=publication_year


    def display(self):
        print(f"Title:{self.title}, Author:{self.author}, Publication:{self.publication_year}")

obj1=Book("Holy Bible","JESUS","since when world created by jesus")       
obj1.display()


class Ebook(Book):
    def __init__(self,file_size,format):
         self.file_size=file_size
         self.format=format

    def display(self):
         print(f"File size:{self.file_size}, File Format:{self.format}")

obj2=Ebook("10mb","Pdf")
obj2.display()

class Printedbook:
     def __init__(self,weight,cover_type):
          self.weight=weight
          self.cover_type=cover_type

     def display(self):
        print(f"Book weight: {self.weight},Book cover:{self.cover_type}")

obj3=Printedbook("500 Grams","Leather cover")
obj3.display()

          


     