# Exercițiul 2: Crearea unei clase Car cu încapsulare

# TODO Scrieți o clasă Python numită Car care demonstrează încapsularea de bază:
"""
Atribute:
    make (șir de caractere)
    model (șir de caractere)
    _speed (număr întreg, atribut privat) - reprezintă viteza curentă (inițial 0)
Metode:
    __init__: Inițializează atributele și setează _speed la 0.
    accelerate: Crește viteza cu o valoare dată.
    brake: Scade viteza cu o valoare dată, asigurându-se că nu scade sub 0.
    get_speed: Returnează viteza curentă (metodă publică pentru accesarea atributului privat).
"""


class Car:
    def __init__(self, make, model):
        self.make=make
        self.model=model
        self.__speed=0
    def accelerare(self, viteza):
        self.__speed+=viteza
    def frana(self, viteza):
        self.__speed-=viteza
        if viteza > self.__speed:
            self.__speed =0
    def get_speed(self):
        return self.__speed

masina1=Car('bmw', 'x1')
masina1.accelerare(20)
masina1.frana(10)
masina1.get_speed()
print(masina1.get_speed())