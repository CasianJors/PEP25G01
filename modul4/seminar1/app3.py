def colecteaza_credentiale():
    credentiale = {}
    for i in range(3):
        utilizator = input(f'Introduceti numele utilizatorului{i + 1}:')
        password = input(f'Introduceti parola{i + 1}:')
        credentiale[utilizator] = password
    return credentiale


def afisare_credentiale(c):
    for utilizator, parola in c.items():
        print(f'{utilizator}->{parola}')


credentiale = colecteaza_credentiale()
afisare_credentiale(credentiale)