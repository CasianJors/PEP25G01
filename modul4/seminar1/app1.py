def check_parola(password):
    lungime = False
    cifra = False
    caracter = False
    upper = False

    if password[0].isupper():
        upper= True
    if len(password) >= 7:
        lungime = True

    for i in password:
        if i.isdigit():
            cifra = True
        if i in ['!', "%", "@"]:
            caracter = True

    if not lungime:
        print("Parola nu are lungime mai mare de 7 caractere")
    if not cifra:
        print("Parola nu contine cifre!!!")
    if not caracter:
        print("Parola nu contine caractere speciale")
    if not upper:
        print("Parola nu incepe cu o majuscula")

    return lungime and cifra and caracter and upper

if __name__ == '__main__':
    username = input("Introduceti userul")
    incercare = 1
    while incercare <= 3:
        print(f'esti la incercarea {incercare}')
        parola = input("Introduceti parola")
        if check_parola(parola):
            print("Ai intrat cu succes")
            break
        else:
            print("Incearca din nou")
            incercare += 1
