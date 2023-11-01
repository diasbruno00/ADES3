
class Graph:

    def __init__(self) -> None:
        self.num_nodes = 0 # numero de nós
        self.num_edges = 0 # numero de aretas 
        self.adj = {} # Grafo


    def add_no(self,node):
        if node not in self.adj: # caso não tenha o no ele irar criar
            self.adj[node] = {}
            self.num_nodes += 1

    def add_edges(self, u, v, weight):
        if u not in self.adj: # caso não tenha o no U ele irar criar
            self.add_no(u)

        if v not in self.adj: # caso não tenha o no V ele irar criar
            self.add_no(v)

        self.adj[u][v] = weight # se ele não caiu nos if  e pq existe um no U e no V entao ele irar relacionar o no U com o no V
        self.num_edges += 1  
    

    def add_twe_way_edge(self, u , v, weigtht): # aqui irar fazer a mesma verificação do add_egnes so que ele vai relacionar U com V e V com U

        self.add_edges(u,v,weigtht)  
 
        self.add_edges(v,u,weigtht)

    def degree_out(self, node): # retorna o grau apenas de saida
        return len(self.adj[node])
    
    def there_is_edge(self,u,v): # verifica se o grafo u " segue " o grafo v
       try:
        return self.adj[u][v]
       except Exception as error:
           print("Não contem")
    
    def defreen_in(self,node): # verifica o grau de um no
        for  chave in self.adj:
            if chave == node:
                return len(self.adj[node])
    
    def neighBors(self,node): # recupera os nos vizinhos de um determinado no
        lista = []
        for chave in self.adj[node]:
            lista.append(chave)
        return lista
    
    def highest_degreen_in(self): # retorna o maior grau do grafo
        lista = [ ]
        for chave in self.adj:
          lista.append( self.defreen_in(chave))
        return max(lista)
    
    def node_with_higest_defrre_in(self): # retorna o no de maior grau
        list = []
        for i, j in self.adj.items():
            list.append(len(j))
        
        maior = max(list)

        for i, j in self.adj.items():
            if len(j) == maior:
                return j
    
    #def density(self): #


    #def complete(self): # verifica se o grafo e completo


    def __repr__(self) -> str:
        str = ""
        for u in self.adj:
            str += f"{u} -> {self.adj[u]}\n"
            
        return str