lista = [2, 8, 7, 88, 21, 35]
print(lista)
for i in range(0, len(lista) -1):
    for x in range(0, len(lista) -i -1):
        if lista[x] > lista[x+1]:
            lista[x], lista[x + 1] = lista[x+1], lista[x]

print(lista)