class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("The Hunger Games", "John Green")
print(book1.title)
print(book1.author)
del book1.author
book1.author = "Suzanne Collins"
print(book1.title)
print(book1.author)
