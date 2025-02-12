print("""1. Cappuccino ... 4 lei
2. Espresso ... 3.5 lei""")

optiune = int(input("Ce optinue alegeti? 1 sau 2: "))
banc = int(input("Introduceti o bancnota. 5 sau 10: "))

if optiune == 1:
    cost = 4
elif optiune == 2:
    cost = 3.5
else:
    cost = 0

if banc in [5,10]:
    print(f"Veti primi restul de {banc - cost} lei")
else:
    print("Bancnota gresita")


