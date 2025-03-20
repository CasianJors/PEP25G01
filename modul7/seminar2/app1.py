# Exercițiul 1: Crearea clasei Animal
"""
# TODO Scrieți o clasă Python numită Animal cu următoarele specificații:

Atribute:
    name (șir de caractere)
    species (șir de caractere)
Metode:
    __init__: Inițializează atributele.
    speak: O metodă care afișează un mesaj generic, de exemplu "Animalul scoate un sunet."
Extindere:
    Creați o subclasă Dog care moștenește clasa Animal. Suprascrieți metoda speak pentru a afișa "Woof!"
     și adăugați o metodă suplimentară fetch care afișează "Aduc mingea...".
"""


class Animal:
    def __init__(self, nume, specie):
        self.nume = nume
        self.specie = specie

    @staticmethod
    def speak():
        print("Animalul face un sunet")

class Dog(Animal):
    def __init__(self, nume):
        super().__init__(nume, 'Caine')

    @staticmethod
    def speak():
        print("Woof!")

    def fetch(self):
        print(self.nume + " a adus mingea")
        self.speak()

Toto = Dog("Toto")
Toto.fetch()        # obiect
