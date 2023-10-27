
def retornaPosicao(array, elemento):
    for i in range(len(array)):
        if(elemento == array[i]):
            return i
    return -1

array = [ 10,11, 12, 13, 14]

posicao = retornaPosicao(array, 15)

print(f'A posição do elemento e : {posicao}')

def falarEuTeAmo(destino,mensagem):
    print(f'Olá {destino} {mensagem}')


falarEuTeAmo('Mariana',' Eu te amo' )
