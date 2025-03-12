stoc = {}


def vizualizare():
    print(stoc)


def adaugare():
    produs = (input('Adaugati un produs;pret;stoc'))
    nume, pret, cant = produs.split(';')
    if produs in stoc:
        print('Produsul exista deja')
    else:
        stoc[nume] = pret, cant


def stergere():
    produs = input('Care este produsul pe care doresti sa il elimini')
    if produs in stoc:
        del stoc[produs]
    else:
        print('Produsul nu se afla in depozitul virtual')


meniu = {
    "1": vizualizare,
    "2": adaugare,
    "3": stergere,
    "4": exit
}

while True:
    optiune = input('''Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire
''')
    assert optiune in meniu
    meniu[optiune]()