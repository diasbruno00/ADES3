
class Graph:

    def __init__(self) -> None:
        self.num_nodes = 0 # numero de nós
        self.num_edges = 0 # numero de aretas 
        self.adj = {}


    def add_no(self,node):
        if node not in self.adj: # caso não tenha o no ele irar criar
            self.adj[node] = {}
            self.num_nodes += 1

    def add_edges(self, u, v, weight):
        if u not in self.adj: # caso não tenha o no U ele irar criar
            self.add_no(u)

        if v not in self.adj: # caso não tenha o no V ele irar criar
            self.add_no(v)

        self.adj[u][v] = weight # se ele não caiu nos if e pq existe um no U e no V entao ele irar relacionar o no U com o no V
        self.num_edges += 1  
    

    def add_twe_way_edge(self, u , v, weigtht): # aqui irar fazer a mesma verificação do add_egnes so que ele vai relacionar U com V e V com U

        self.add_edges(u,v,weigtht)  

        self.add_edges(v,u,weigtht)
    