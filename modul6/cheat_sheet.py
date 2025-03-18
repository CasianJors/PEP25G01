"""
Concepte clase
"""
# # ========================================================
# # Declararea unei clase si initializarea unui constructor
# # ========================================================

class A:
    def __init__(self):
        print("Eu sunt A")

# # ========================================================
# # Instantierea unui obiect de tip A
# # ========================================================

a = A           # fara parantezele de initializare, a ia valoarea clasei in sine
print(a)

a = A()         # apelarea constructorului = instantierea unui obiect

# # ========================================================
# # Constructori parametrizati
# # ========================================================
class Masina:

    def __init__(self, marca, culoare):
        self.marca = marca
        self.culoare = culoare

# # ========================================================
# # Accesarea atributelor
# # ========================================================

masina1 = Masina("Audi", "negru")
masina2 = Masina("Peugeot", "alb")

print(masina1.marca)        # acceseaza marca obiectului masina1
print(masina2.marca)        # acceseaza marca obiectului masina2


# # ========================================================
# # Destructori
# # ========================================================

class Masina:

    def __init__(self, marca, culoare):
        self.marca = marca
        self.culoare = culoare

    def __del__(self):
        print(f"Masina {self.marca} a fost stearsa.")

masina1 = Masina("Audi","negru")
masina2 = Masina("Peugeot", "alb")
#
# # ========================================================
# # Parametrii default la atribute
# # ========================================================
class Masina:

    def __init__(self, marca, culoare = "alb"):
        self.marca = marca
        self.culoare = culoare

    def __del__(self):
        print(f"Masina {self.marca} a fost stearsa.")


masina3 = Masina("Audi", "negru")
masina4 = Masina("Peugeot")

print(masina2.culoare)

# # ========================================================
# # Exercitiu:
# # todo:
# #  Creati o clasa Laptop cu urmatoarele atribute:
# #  marca, model, procesor, memorie
# #  - Creati 5 obiecte de tip Laptop la alegere.
# #  - Afisati numele marcilor care au procesoare > i3
# # ========================================================

"""
Metode de clasa si metode de instanta
Atribute de clasa si atribute de instanta
"""
class Animal:

    animale = []

    def __init__(self, nume, varsta, culoare):
        self.nume = nume
        self.varsta = varsta
        self.culoare = culoare

    @classmethod
    def afisare_animale(cls):
        for i in cls.animale:
            print(f"-- Nume: {i.nume}")
            print(f"-- Varsta: {i.varsta}")
            print(f"-- Culoare: {i.culoare}")


# # ========================================================
# # Encapsularea atributelor
# # ========================================================
class Animal:

    def __init__(self, nume, culoare, varsta):
        self.nume = nume
        # privat
        self.__culoare = culoare
        # protected
        self._varsta = varsta

    def getCuloare(self):
        return self.__culoare

    def setCuloare(self, culoare):
        self.__culoare = culoare

animal1 = Animal("Tasha", "alb", "4")



"""
Mostenirea
"""
# # ========================================================
# # Mostenirea unica
# # ========================================================
class A:

    def __init__(self, i):
        self.i = i

    def putere_i(self):
        return self.i ** 2

class B(A):

    def __init__(self, i):
        super().__init__(i)


b = B(7)
print(b.putere_i())


# # ========================================================
# # Execitiu:
# # todo: Care va fi outputul urmatorului cod?
# # ========================================================
class A:
    def __init__(self):
        self.calcul(30)

    def calcul(self, i):
        self.i = 2 * i
        print("i from A is", self.i)

class B(A):
    def __init__(self):
        super().__init__()
        print("i from B is", self.i)

    def calcul(self, i):
        self.i = 3 * i

b = B()

# # ========================================================
# # Mostenire multipla
# # ========================================================
class A:

    def __init__(self):
        print("Clasa A")

class B:

    def __init__(self):
        print("Clasa B")

class C(A,B):

    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Clasa C")

c = C()

# # ========================================================
# # Mostenire pe mai multe nivele
# # ========================================================
class A:

    def __init__(self):
        print("Clasa A")

class B(A):

    def __init__(self):
        super().__init__()
        print("Clasa B")

class C(B):

    def __init__(self):
        super().__init__()
        print("Clasa C")

b = B()
c = C()

# # ========================================================
# # Mostenire ierarhica
# # ========================================================

class A:

    def __init__(self):
        print("Clasa A - clasa mama")

class B(A):

    def __init__(self):
        super().__init__()
        print("clasa B")

class C(A):

    def __init__(self):
        super().__init__()
        print("Clasa C")

b = B()
c = C()
