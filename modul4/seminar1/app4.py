angajat1 = {
    'nume': 'Ana-Maria Popescu',
    'departament': 'IT',
    'ID': 3409,
    'Salar': 4560,
}
angajat2 = {
    'nume': 'Marian Muntean',
    'departament': 'IT',
    'ID': 2235,
    'Salar': 4556,
}
angajat3 = {
    'nume': 'Maria Manea',
    'departament': 'HR',
    'ID': 1908,
    'Salar': 6755,
}
angajat4 = {
    'nume': 'Oana Popa',
    'departament': 'HR',
    'ID': 1977,
    'Salar': 5400,
}
angajat5 = {
    'nume': 'David Codru',
    'departament': 'Management',
    'ID': 1988,
    'Salar': 12900,
}

lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]

# a.
for angajat in lista_dict:
    if angajat['Salar'] > 5000:
        print(angajat['nume'], " -> ", angajat['departament'] + str(angajat['ID']))

# #b.

lista_angaj = []

for angajat in lista_dict:
    if angajat['departament'] != "Management":
        lista_angaj.append(angajat['nume'])

print(lista_angaj)

# c.

mean_sal = []

for angajat in lista_dict:
    if angajat['departament'] == "HR":
        mean_sal.append(angajat['Salar'])

print("Media salariala a departamentului de HR este: ", sum(mean_sal) / len(mean_sal))