class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):  # Magic method - pretty much overwrites a 'included' method 
        return self.title + " by " + self.author
    
    def __len__(self):
        return self.pages
    
    def __del__(self):  # Still deletes the object but also prints a confirmation
        print("A book object has been deleted!")

book1 = Book("First Book", "SK", 500)

print(book1)
del(book1)
print(book1)