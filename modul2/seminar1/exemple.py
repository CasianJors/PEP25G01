"""
Tipuri de date in Python
"""

str1 = "Text"                                               # String
int1 = 5                                                    # Nr intreg
float1 = 5.                                                 # Numar cu virgula mobila
lista1 = [1,"2",3.]                                          # lista
dict1 = {"produs": "masa", "pret": 550, "stoc": 5}          # Dictionar
bool1 = True                                                # boolean
byte1 = bytes(56)                                           # binar


"""
Afisarea tipului de date de care apartine variabila declarata
"""
print(type(str1))
print(type(int1))
print(type(float1))
print(type(lista1))
print(type(dict1))
print(type(bool1))
print(type(byte1))


"""
Afisarea capabitatilor (a metodelor) variabilei
"""
print(dir(str))         # capabilitatile unui string
print(dir(int1))        # capabilitatile variabilei int1 (aka capabilitatile unui int)


"""
Afisarea locatiei in memorie a unei variabile
"""
print(id(lista1))       # locatia in decimal
print(hex(id(str1)))    # locatia in hexadecimal


"""
# ===================================================
# Mutable data types - list, dict, bytearray, class
# ===================================================
"""

lista_muabila = [1,2,3]
print(lista_muabila)            # afiseaza lista
print(id(lista_muabila))        # afiseaza locatia listei in memorie

lista_muabila[0] = 5            # schimbam valoarea elementului de pe pozitia 0 cu 5
print(lista_muabila)
print(id(lista_muabila))        # locatia listei in memorie ramane neschimbata => se pastreaza identitatea obiectului

"""
#  ====================================================================
#  Immutable data types - int, float, str, complex, bool, tuple, bytes
#  ====================================================================
"""

string_imuabil = "text"
print(string_imuabil)           # afiseaza variabila
print(id(string_imuabil))       # afiseaza locatia in memorie a variabilei

string_imuabil = string_imuabil + "s"   # concatenam valoarea variabilei cu un alt string "s"
print(string_imuabil)
print(id(string_imuabil))       # locatia in memorie este schimbata => se creaza o variabila noua cu valoarea schimbata

"""
 ====================================
 Functia print() - output pe consola
 ====================================
"""

print(string_imuabil)                                           # afisarea valorii stocate intr-o variabila
print("Textul acesta nu a fost stocat intr-o variabila")        # afisarea unei valori
print(3 + 4)                                                    # afisarea rezultatului unui calcul
print("Rezultatul este: ", 3 + 7)                               # afisarea mai multor elemente separate prin virgula

"""
 ====================================
 Functia input() - input pe consola
 ====================================
"""

raspuns = input("Introduceti un numar: ")       # In interiorul functiei specificam un prompt
print(raspuns)                                  # raspunsul utilizatorului va fii stocat in variabila raspuns
print(type(raspuns))


"""
Tipuri de date numerice
"""

"""
 Transformarea unui sir care contine doar cifre in numar intreg
"""
str_numeric = "5"
print(type(str_numeric))
int_numeric = int(str_numeric)
print(type(int_numeric))

"""
Transformarea unui sir care contine doar cifre in numar intreg
"""
str2_numeric = "6.7"
print(type(str2_numeric))
float_numeric = float(str_numeric)
print(type(float_numeric))

"""
 Valori boolene
"""
a = 0
print(bool(a))          # numerele pot fi transformate in valori boolene, unde 1 = True, 0 = False

b = None                # None este valoarea nula in Python si va fii False mereu
print(bool(b))


d = True                # True = 1, False = 0 cand transformam in int
print(int(d))
e = False
print(int(e))

"""
 Operatori aritmetici cu numere int si float
"""
a = 5
b = 5
print(a + b)        # Adunare
print(a - b)        # Scadere
print(a * b)        # a ori b
print(a / b)        # a impartit la b = returneaza numar cu virgula
print(a // b)       # a impartit la b = returneaza numar intreg
print(a ** b)       # a la puterea b
print(a % b)        # returneaza restul impartirii intre a si b

"""
 Operatori relationali cu numere int si float
"""
print(a < b)        # True daca a mai mic ca b, False altfel
print(a <= b)       # True daca a mai mic sau egal cu b, False altfel
print(a > b)        # True daca a mai mare ca b
print(a >= b)       # True daca a mai mare sau egal cu b
print(a == b)       # True daca valoarea lui a este egala cu valoarea lui b
print(a != b)       # True daca valoarea lui a este diferita de valoarea lui b
print(a is b)       # True daca identitatea obiectului este aceeasi (locatia in memorie)
print(a is not b)   # true daca identitatea obiectului nu este aceeasi

"""
Siruri
"""
string1 = "Acesta este un sir"
string2 = 'Acesta este un sir'

string3 = 'Acesta este un "sir".'
string4 = "Acesta este un 'sir'."

"""
# # Escape character = \
"""
# # - pentru a "scutii" urmatorul caracter de la a fii luat in considerare in anumite situatii specifice
# # - iau anumite actiuni in functie de combinatia de caractere

print("Mergem la \"scoala?\"")              # " nu sunt considerate delimitarea sirului
print("C:\\User\\local\\Python")            # \ nu este considerat escape character
print("1\n2\n3\n4\n")                       # linie noua
print("Bun\tvenit\tla\tcursul\tPython")     # tab
print("Pythonnnnn \b")                      # backspace

"""
 Manipularea sirurilor
"""
x = 5
print(type(str(x)))               # Transforma elementul in str

#
print("ABCD" + "EFGH" + str(6))   # Concatenarea sirurilor = TREBUIE SA FIE STR TOATE ELEMENTELE CONCATENATE (daca nu sunt => str(i))
print(string1 + string2)

print(string1 * 3)          # multiplica sirul

print(string1[0])           # extragerea cracterelor din sir

print(string1[:4])          # extragerea caracterelor de la elementul 0 (default) pana la elementul de pe pozitia 4
print(string1[3:6])         # extragerea caracterelor intre pozitia 3 si 6 - 1
print(string1[::])          # extragerea de la 0 (default) pana la capat(default)
print(string1[::2])         # extragerea de la 0 pana la capat cu salt de 2 (din 2 in 2 caractere)
print(string1[::-1])        # inversarea sirului

print(len(string1))         # afiseaza lungimea sirului intr-un numar intreg

"""
 Afisarea sirurilor
"""

print("Mesaj: " + string1)                      # Concatenare
print("mesaj:",string1)                         # Afiseaza elementele enumerate folosind ca delimitator spatiul (default)
print("Mesaj:",string1,string2,string3,sep="_") # Afiseaza elementele enumerate folosind separatorul dat
print("Mesaj:",string1,end="...")               # Pune la finalul elementelor "...", by default: end="\n"

"""
 Formatarea sirurilor
"""

valoare = input("Cati ani aveti? ")
print(f"Utilizatorul are {valoare} ani.")                                                                # formatare cu f
print("Utilizatorul are {} ani.".format(valoare))                                                        # formatare cu metoda de sir format()
print("Utilizatorul are {} ani si in anul 2027 va avea {} ani.".format(valoare, int(valoare) + 5))
