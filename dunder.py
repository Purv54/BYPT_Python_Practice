# dunder or magic methods are special methods in Python that start and end with double underscores. 
# They are used to define the behavior of objects in Python. For example, 
# the __init__ method is called when an object is created,
#  and the __str__ method is called when an object is printed.

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
b = Book("Python 101", "Purv", 200)

print(b) # this will call the __str__ method and print "Python 101 by Purv"
print(len(b)) # this will call the __len__ method and print 200