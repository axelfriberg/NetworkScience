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

karateclub = nx.read_gml("karate.gml")

#analyzing dataset

# calculating average degree

N,K = karateclub.order(), karateclub.size()
print("degree of node 1: ", karateclub.degree(1))
avg_deg = float(K)/N
print("Nodes: ", N)
print("Edges: ", K)
print("Average degree: ", avg_deg)

#clustering coefficients
print("clustering coefficient node 1: ", nx.clustering(karateclub,1))
print("average clustering coefficient", nx.average_clustering(karateclub))
#Betweenness centrality
print("betweenness centrality of node 1: ", nx.betweenness_centrality(karateclub)[1])
def avg_betw_centr(graph):
    i = 1
    a = 0
    N = int(graph.order())
    while i < N+1:
        a = a + float(nx.betweenness_centrality(graph)[i])
        i = i + 1
    avg = float(a)/float(graph.order())
    print("average betweenness centrality: ", avg)
avg_betw_centr(karateclub)
#Closeness centrality
print("closeness centrality of node 1: ", nx.closeness_centrality(karateclub, 1))
def avg_close_centr(graph):
    i = 1
    a = 0
    N = int(graph.order())
    while i < N+1:
        a = a + float(nx.closeness_centrality(graph)[i])
        i = i + 1
    avg = float(a)/float(graph.order())
    print("average closeness centrality: ", avg)
avg_close_centr(karateclub)

#Eigenvector centrality
print("eigenvector centrality of node 1: ", nx.eigenvector_centrality(karateclub)[1])
def avg_eigenv_centr(graph):
    i = 1
    a = 0
    N = int(graph.order())
    while i < N+1:
        a = a + float(nx.eigenvector_centrality(graph)[i])
        i = i + 1
    avg = float(a)/float(graph.order())
    print("average eigenvector centrality: ", avg)
avg_eigenv_centr(karateclub)

#degree centrality
print("degree centrality node of node 1: ", nx.degree_centrality(karateclub)[1])
def avg_degr_centr(graph):
    i = 1
    a = 0
    N = int(graph.order())
    while i < N+1:
        a = a + float(nx.degree_centrality(graph)[i])
        i = i + 1
    avg = float(a)/float(graph.order())
    print("average degree centrality: ", avg)
avg_degr_centr(karateclub)

#dispersion of graph
print("dispersion between node 1 and 2: ", nx.dispersion(karateclub,1,2))

#histogram of degree distribution
degree_sequence=sorted(nx.degree(karateclub).values(),reverse=True)
dmax = max(degree_sequence)
plt.loglog(degree_sequence,'b-',marker='o')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")
Gcc = sorted(nx.connected_component_subgraphs(karateclub), key=len, reverse=True)[0]
pos = nx.spring_layout(Gcc)
#nx.draw_networkx_nodes(Gcc, pos, node_size=20)
#nx.draw_networkx_edges(Gcc, pos, alpha=0.4)

plt.show()
