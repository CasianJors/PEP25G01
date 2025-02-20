sir = input("Introduceti un sir de numere separate prin virgula: ")
doar_numere = []
lista = sir.split(',')

for element in lista:
    element = element.strip()
    if element.isdigit() and int(element) in range(100):
        doar_numere.append(int(element))

while True:
    optiuni = input(
        """    1. Fiecare numar la puterea y
    2. Suma tuturor numerelor din lista
    3. Inmultirea fiecarui numar cu y
    4. Iesire
    Alegeti optiunea: """
    )

    if int(optiuni) == 1:
        y = int(input("Alege puterea: "))
        for element in doar_numere:
            print(element ** y)
    elif int(optiuni) == 2:
        print(sum(doar_numere))
    elif int(optiuni) == 3:
        yy = int(input("Mai da un nr: "))
        for element in doar_numere:
            print(element * yy)
    elif int(optiuni) == 4:
        print("Iesi acas")
        break
    else:
        print("Optiune invalida, incearca din nou.")
