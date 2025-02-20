numere_castigatoare = [4, 12, 31, 17, 22, 25]
numere_alese = []
numere_alese_castig = []

while len(numere_alese) < 6:
    nr = input("Alege un numar: ")
    if nr.isdigit() and 0 < int(nr) < 50 and int(nr) not in numere_alese:
        numere_alese.append(int(nr))
        if int(nr) in numere_castigatoare:
            numere_alese_castig.append(int(nr))
    else:
        print("Numar invalid")

if len(numere_alese_castig) == 2:
    premiu = "50 lei"
elif len(numere_alese_castig) == 3 or len(numere_alese_castig) == 4:
    premiu = "500 lei"
elif len(numere_alese_castig) == 5:
    premiu = "1000 lei"
elif len(numere_alese_castig) == 6:
    premiu = "5000 lei"
else:
    premiu = "0 lei"

print(
    f"Numerele tale alese sunt {numere_alese}, "
    f"dintre care cele castigatoare sunt {numere_alese_castig}. "
    f"Felicitari, ai castigat {premiu}"
)
