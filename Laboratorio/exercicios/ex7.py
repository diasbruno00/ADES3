
def calcularVogais(palavra):
    palavra = palavra.lower()
    vogais = ['a','e','i','o','u']
    contador = 0
    for  letra in palavra:
        for vogal in vogais:
            if(letra == vogal):
                contador = contador + 1
    
    return  contador
    

palavra  = 'Alemanha'
quantidadeVogais  = calcularVogais(palavra)

print(f'A quantidade vogais na string {palavra} e {quantidadeVogais}')