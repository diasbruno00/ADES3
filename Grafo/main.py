from graph import Graph


g = Graph()


g.add_twe_way_edge("Bia", "Ana", 0)
g.add_twe_way_edge("Caio", "Ana", 0)
g.add_twe_way_edge("Caio", "Duda", 0)
g.add_twe_way_edge("Caio", "Bia", 0)



print(g.adj)