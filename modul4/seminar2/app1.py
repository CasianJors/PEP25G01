def suma(lista: list):
    print('Ati ales optiunea 2')
    print(f'suma este {sum(lista)}')

def medie(lista: list):
    print('Ati ales optiunea 1')
    print(f'media este {sum(lista) / len(lista)}')

def putere(lista: list):
    print('Ati ales optiunea 3')
    for i in lista:
        print(i**2)

def iesire(lista):
    print('Goodbye')
    exit()

def gresit(lista):
    print("ai ales gresit :O")

meniu = {
    "1": medie,
    "2": suma,
    "3": putere,
    "4": iesire
}

def get_numere():
    numere = []
    while True:
        try:
            numar = float(input("introduce un numar"))
            numere.append(numar)
        except Exception as mesaj_eroare:
            if "'x'" in str(mesaj_eroare):
                break
            else:
                print(mesaj_eroare)
    return numere

def afiseaza_meniu():
    print("""Meniu:
1. Media numerelor
2. Suma numerelor
3. Puterea numerelor din lista de numere
4. Iesire""")
    return input('Incroduceti optiunea')


while True:
    lista = get_numere()
    optiune = afiseaza_meniu()
    operatie = meniu.get(optiune, gresit)
    operatie(lista)


