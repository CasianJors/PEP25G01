with open("cuvinte.txt", "r") as file:
    randuri = file.readlines()
print(randuri)

dictionar = {}
for rand in randuri:
    rand.replace(" \n", '')
    index,litera = rand.split(':')
    dictionar[index] = litera.strip()

for elem,index in dictionar.items():
    print(elem, index, sep='')