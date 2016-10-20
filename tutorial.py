import networkx as nx

G=nx.Graph()

G.add_node(1)
G.add_node(4)

G.add_nodes_from([2,3])

H = nx.path_graph(10)

G.add_nodes_from(H)

G.add_edge(1,3)

G.add_node("spam")

print("Number of nodes: " + str(G.number_of_nodes()))

print("Numder of edges: " + str(G.number_of_edges()))

print("The nodes in the graph: " + str(G.nodes()))

print("Neighbors of node 3:" + str(G.neighbors(3)))

H = nx.DiGraph(G)

print(list(H.edges()))

G.graph["Title"] = "Tutorial"

mygraph = nx.read_gml("karate.gml")

print(nx.clustering(mygraph))
print(nx.average_clustering(mygraph))
