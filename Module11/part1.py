class Publi:
    def __init__(self, name):
        self.name = name

class Book(Publi):
    def __init__(self, name, author, side_view):
        super().__init__(name)
        self.author = author
        self.side_view = side_view

    def output(self):
        print(f"BOOK: {self.name}")
        print(f"Author: {self.author}")
        print(f"Side view: {self.side_view}")

class News(Publi):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def output(self):
        print(f"NEWS: {self.name}")
        print(f"Editor: {self.editor}")

news1 = News("111", "22")
book1 = Book("wwqds", "dsa", 20)

news1.output()
print("_" * 50)
book1.output()
