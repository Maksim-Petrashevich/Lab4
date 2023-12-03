class Book:
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year=year

    def display(self):
        return f"Книга: {self.title}, Автор: {self.author}, Год издания: {self.year}"

    def get_year(self):
        return self.year

    @staticmethod
    def visokosny(year):
        return (year % 4 == 0 and year %100 != 0 ) or (year %400 == 0)

    @classmethod
    def janr(cls):
        return "Роман"

if __name__ == '__main__':
    book1= Book("Война и мир", "Лев Толстой", 1869)
    print(book1.display())
    year = book1.get_year()
    print(f"Год {year}{' высокосный' if Book.visokosny(year) else ' не высокосный'}")
    print(f"Жанр книги: {Book.janr()}")
