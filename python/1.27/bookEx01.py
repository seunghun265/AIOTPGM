class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
        
    def __str__(self):
        return f"제목 = {self.title}, 페이지 수 = {self.pages}"
    
    def __add__(self,other):
        return Book(self.title + other.title, self.pages + other.pages)
    
    def __gt__(self,other):
        return self.pages > other.pages
    
book1 = Book("어린왕자",430)
book2 = Book("1984",500)
print(book1)
print(book2)
print(book2+book1)