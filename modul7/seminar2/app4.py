# Exercițiul 4: Debugging - Găsește erorile din clasa următoare

# TODO Examinați codul de mai jos și identificați cel puțin trei erori. Corectați-le astfel încât codul să ruleze corect.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        print("Title: " + self.title)
        print("Author: " + self.author)

    def set_title(self, new_title):
        self.title = new_title

# Crează o instanță și încearcă să actualizezi titlul
my_book = Book("1984", "George Orwell")
my_book.set_title("Animal Farm")
my_book.get_info()

"""
Indicații:
    - Verificați parametrii metodelor (ex. lipsa lui self la set_title).
    - Observați modul corect de a defini metodele în interiorul unei clase.
    - Asigurați-vă că apelurile metodelor sunt efectuate pe obiectul corespunzător.
"""

