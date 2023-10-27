
array = [ 10, 10, 20, 30 ,10]


def retornaMedia(array):
    soma = 0
    media = 0
    for numero in array:
        soma += numero 
    media = soma / len(array)
    return media


media = retornaMedia(array)

print(f'A media do array: {media}')

