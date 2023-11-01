from graph import Graph

g = Graph()
g.add_twe_way_edge("Ana", "Bia", 1)
g.add_twe_way_edge("Ana", "Caio", 1)
g.add_twe_way_edge("Caio", "Bia", 1)
g.add_twe_way_edge("Caio", "Duda", 1)
g.there_is_edge("Duda", "Bia")
print(g.defreen_in("Ana"))
lista = g.neighBors("Ana")
print(lista)
print(g.highest_degreen_in())
print(g.node_with_higest_defrre_in())