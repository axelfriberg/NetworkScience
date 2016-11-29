import networkx as nx
import re

num_edges = 2312497
current_edges = 0

G=nx.Graph()
file = open("web-Stanford.txt", 'r')
lines = file.readlines()
lines = lines[4:] # Remove the instructional lines

print("Adding edges to graph...")

for line in lines:
    split_line = re.split(r'\t+', line.rstrip('\n'))
    G.add_edge(split_line[0], split_line[1])
    current_edges += 1
    print("Added " + str(current_edges) + "/" + str(num_edges) + " of total edges.", end="\r")

file.close()

print("\nDone")
