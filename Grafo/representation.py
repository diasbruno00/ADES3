 #0 1 2 3   // linha  e coluna  Matriz de adj
g = [[0,1,1,0],
     [1,0,1,0],
     [1,1,0,1],
     [0,0,1,0]]

print(f'Há ligação de 2 para 3 ? {g[2][3]}')

def retornaVizinhos(posicao):
    list = []
    for numero in g[posicao]:
        if(numero != 0):
            list.append(numero)
    return list


print(retornaVizinhos(2))

# Lista de ajacência

g2 = [[1,2],
      [0,2],
      [0,1,3]
      ,[2]]

def verificandoLigacao(g, posicao, numeroEncontrar):
    for numero in g[posicao]:
        if numero == numeroEncontrar:
            return True
    return False


print(verificandoLigacao(g2, 2, 3))


grafo = {"Ana": {"Bia": 5, "Caio": 6},
         "Bia": {"Ana": 5, "Caio": 8},
         "Caio": {"Ana": 6, "Bia": 8, "Duda": 7},
         "Duda": {"Caio": 7}}


print("Caio" in grafo["Bia"])
print("Bia" in grafo["Caio"])