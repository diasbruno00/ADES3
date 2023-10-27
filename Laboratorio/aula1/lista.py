
listaDeFrutas = ['Uva', 'Maça', 'Banana', 'Pera']

print(listaDeFrutas[1])
print(listaDeFrutas[1:3])
print(listaDeFrutas[3])
print(listaDeFrutas[-1])
print(listaDeFrutas[0:2] + listaDeFrutas[2:3])

listaDeFrutas.append('Kiwi')
listaDeFrutas.pop(1)
listaDeFrutas.remove('Uva')
listaDeFrutas.insert(0, 158)
listaDeFrutas += ["Manga"]

print("Pera" in listaDeFrutas) # O(n) => Busca Sequencial

print(listaDeFrutas.index("Pera"))

# range (inicio, fim , passo)
for i in range(len(listaDeFrutas)):
    print(listaDeFrutas[i])


for fruta in listaDeFrutas:
    print(fruta)

