
class Graph:

    def __init__(self) -> None:
        self.num_nodes = 0 # numero de nós
        self.num_edges = 0 # numero de aretas 
        self.adj = {}


    def add_no(self,node):
        if node not in self.adj:
            self.adj[node] = {}
            self.num_nodes += 1

    def add_edges(self, u, v, weight):
        if u not in self.adj:
            self.add_no(u)

        if v not in self.adj:
            self.add_no(v)

        self.adj[u][v] = weight
        self.num_edges += 1  
    

    def add_twe_way_edge(self, u , v, weigtht):

        self.add_edges(u,v,weigtht)

        self.add_edges(v,u,weigtht)
    