lista = input("Introduceti lista de taskuri: ")
lista_taskuri = lista.split(",")

print(lista_taskuri)
lista_fara_dubluri=[]
for task in lista_taskuri:
    if task in lista_fara_dubluri:
        continue
    else:
        lista_fara_dubluri.append(task)

print(lista_fara_dubluri)