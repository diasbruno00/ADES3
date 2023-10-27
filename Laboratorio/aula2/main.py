# similar a tabela hash
codigosPaises = {
    'BR': "Brazil",
    'US': 'United States',
    "SP": 'Spain'
}
codigosPaises['DE'] = 'Deutschland'
#print(codigosPaises['FR']) erro

codigosPaises.pop('BR')

t = {
    'pt': {
        'ball': 'bala',
        'cas': 'carro'
    },
    'en': {
        'ball': 'ball',
        'cas': 'cas'
    }
}

#print(t['pt']['cas'])

grafo = { 'ana': ['caio', 'bia'], 
        'bia': ['ana'],
        'caio': ['ana']}

for chave, valor in grafo.items():
    if chave == 'ana':
        for v in valor:
            print(v)

dicionarioNotas = {
'notas': [],
 'frequencia': [2]

}
soma = 0
media = 0
for i in range(0,3,1):
  
    dicionarioNotas['notas'].append(int(input(f'nota {i+1}: ')))

    soma = sum(dicionarioNotas['notas'])
           
media = soma / len(dicionarioNotas['notas'])
print(media)
print(dicionarioNotas['notas'])


def find_min(array):
    min = 0
    max = 0
    for num  in array:
        if num > max:
            max = num
        else:
            min = num


    return (min, max)


(min, max ) = find_min([29,90,21,4])

