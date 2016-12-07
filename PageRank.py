import networkx as nx
import matplotlib.pyplot as plt

num_edges = 5
current_edges = 0

G = nx.Graph()
file = open("ExampleGraph.txt", 'r')
lines = file.readlines()

print("Adding edges to graph...")

for line in lines:
    split_line = line.split()
    G.add_edge(int(split_line[0]), int(split_line[1]))
    current_edges += 1
    print("Added " + str(current_edges) + "/" + str(num_edges) + " of total edges.", end="\r")

file.close()
print("\nDone")

pr_dict = nx.pagerank(G)
print(pr_dict)

plt.bar(range(len(pr_dict)), pr_dict.values(), 0.5, align='center')
plt.xticks(range(len(pr_dict)), {'A', 'B', 'C', 'D'})

plt.ylim(0, 1)
plt.savefig("PageRankValues.png")
