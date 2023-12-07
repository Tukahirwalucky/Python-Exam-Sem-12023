#creat a python class named book with attributes

class Book:
    def __init__(self, title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

#new instict of the class.
book_title=("great expaectations") 
book_author=("charles dicken")
book_pages=(2000)
print(book_title)
print(book_author)
print(book_pages)


def book_title_and_author():
    output=("great epectations", "charles dicken")
    print(output)
    
book_title_and_author()   




        