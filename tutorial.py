import networkx as nx
import matplotlib.pyplot as plt
import collections

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

#analyzing dataset

print(nx.clustering(mygraph))
print(nx.average_clustering(mygraph))
#Betweenness centrality
print(nx.betweenness_centrality(mygraph))
#Closeness centrality
print(nx.closeness_centrality(mygraph))
#Eigenvector centrality
print(nx.eigenvector_centrality(mygraph))
#degree centrality
print(nx.degree_centrality(mygraph))
#dispersion of graph
print(nx.dispersion(mygraph))


# calculating average degree

N,K = mygraph.order(), mygraph.size()
avg_deg = float(K)/N
print("Nodes: ", N)
print("Edges: ", K)
print("Average degree: ", avg_deg)

#histogram of degree distribution (not done yet)

#degrees = mygraph.degree()
#values = sorted(set(degrees.values()))
#hist = []

#plt.figure()
#plt.plot(degrees, hist, 'ro')
#plt.legend(['Degree'])
#plt.xlabel('Degree')
#plt.ylabel('Number of nodes')
#plt.title("Zachary's Karate Club")
#plt.savefig('Degree_distribution_Karate_Club.pdf')
#plt.show()
