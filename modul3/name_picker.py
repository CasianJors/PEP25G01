import random
import time as t

def main():
    names = [
        "Andreea Laus", "Denisa-Petronela Grecu", "Diana Muresan", "Murariu Gabriel", "Perianu Rares",
        "Andreea Mihaela Milosescu", "Vladia Alin", "Gabriela Danciuloiu", "Petcu Cristina Larisa",
        "Trendo Ionut Raul", "Furca Andrei", "Cristina Coșa", "Cosmin Alexandru Arsa"
    ]

    chosen_name = random.choice(names)
    t_end = t.time() + 3
    print("loading", end="")
    while t.time() < t_end:
        print(".", end= ".")
        t.sleep(0.1)

    print("\n", chosen_name)


if __name__ == '__main__':
    main()
