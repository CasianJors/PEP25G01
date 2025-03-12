lst = []

while True:
    numar = input("Introduceti un numar (cand v-ati saturat, apasati q): ")
    if numar == 'q':
        break
    try:
        numar = int(numar)
    except ValueError:
        print("Introduce un numar corect!")
    else:
        lst.append(numar)

# Suma numarului de pe pozitia 1 si 2.
print("O sa adaugam numarul 2 si 3.")
try:
    print("lst[1] + lst[2] = ", lst[1] + lst[2])
except IndexError:
    print(f"Lista ta are doar {len(lst)} elemente")
except Exception as mesaj:
    print(f"A aparut o eroare neasteptata: {mesaj}")

# Divizia primelor 2 numere din lista
print("Divizia primelor 2 numere din lista este: ")
try:
    print("lst[0] / lst[1] = ", lst[0] / lst[1])
except IndexError:
    print(f"Lista ta are doar {len(lst)} elemente")
except ZeroDivisionError:
    print(f"Impartirea cu 0 nu este posibila inca: {lst[0]} : {lst[1]}")
except Exception as mesaj:
    print(f"A aparut o eroare neasteptata: {mesaj}")


# Suma tuturor numerelor din lista
sum = 0
for i in lst:
    sum += i
print("Suma tuturor numerelor din lista este: ", sum)
