import time
import random


def inputul_jucatorului():
    numere_jucator = []
    while len(numere_jucator) < 6:
        try:
            numar = int(input("Introduceti un numar"))
        except Exception:
            print("Nu e bun numarul")
        else:
            if 0 < numar <= 49 and numar not in numere_jucator:
                numere_jucator.append(numar)
            else:
                print("Nu e bun numarul")

    return numere_jucator

def numere_castigatoare():
    optiuni = list(range(1,50))
    castigatoare = []
    for _ in range(6):
        selectie = random.choice(optiuni)
        optiuni.remove(selectie)
        castigatoare.append(selectie)
    return castigatoare

def afisare_rezultat(jucator, robot):
    jucators = set(jucator)
    robots = set(robot)
    castig = len(jucators.intersection(robots))
    print(" Numerele tale sunt ", jucator)
    print("Numere castigatoare sunt:")
    for i in range(6):
        print('...', end='')
        time.sleep(1.5)
        print(robot[i], end='')

    time.sleep(1.5)
    print()
    if castig == 0:
        print("Mai joaca. Ai pierdut")
    elif castig < 4:
        print("Ai castigat 50 de lei")
    elif castig < 6:
        print("Ai castigat 500 de lei")
    else:
        print("Ai castigat 1500 de lei")


if __name__ == '__main__':
    jucator = inputul_jucatorului()
    robot = numere_castigatoare()
    afisare_rezultat(jucator, robot)