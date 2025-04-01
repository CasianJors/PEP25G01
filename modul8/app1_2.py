from app1 import EnumeratorCuvant

user = input("Introduceti un cuvant")

for i, litera in EnumeratorCuvant(user):
    if litera.isalpha():
        with open("cuvinte.txt", 'a') as file:
            file.write(f"{i}: {litera} \n")