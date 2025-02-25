def putere(numar=0):
    return numar ** numar

while True:
    numar = input("Introduceti un numar: ")
    if numar == "q":
        break
    if numar.isdigit():
        numar = int(numar)
        print(putere(numar))
    else:
        print("Numar invalid")

print("ai iesit din exercitiu")
