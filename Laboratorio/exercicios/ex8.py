
def retornaSomaElementos(array: list):
    soma = 0
    for num in array:
        soma += num
    return soma

def retornaMaiorANDMenor(array):
    min = 0
    max = 0
    for num  in array:
        if num > max:
            max = num
        else:
            min = num


    return (min, max)

somatorio = retornaSomaElementos([12,13,14,1])

print(f'O somatorio: {somatorio}')

numero: int = 30

for i in range(1,10,1):
    print(i)