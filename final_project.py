import numpy as np
import networkx as nx
from networkx.algorithms import community #use community algorithm to detec communities within a graph
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt


FielName="email-Eu-core-temporal.txt"

Graphtype=nx.DiGraph()   # use net.Graph() for undirected graph

# How to read from a file. Note: if your egde weights are int, change float to int.
G = nx.read_edgelist(FielName, create_using=Graphtype, nodetype=int, data=(('weight',float),))


# Find the total number of degree, in_degree and out_degree for each node
single_outs = 0
list_of_singles = []
for x in sorted(G.nodes()):
    if G.degree(x) == 1:
        single_outs = single_outs + 1
        list_of_singles.append(x)
    elif G.out_degree(x) == 1:
        if x in list_of_singles:
            single_outs = single_outs+1
        else:
            list_of_singles.append(x)
            single_outs = single_outs+1

    print ("Node: ", x, " has total #degree: ",G.degree(x), " , In_degree: ", G.out_degree(x)," and out_degree: ", G.in_degree(x))

# returns all single nodes 
print(single_outs)
print(list_of_singles)

get_edges = False
if get_edges == True:
    # Find the weight for each node
    for u,v in G.edges():
          print ("Weight of Edge ("+str(u)+","+str(v)+")", G.get_edge_data(u,v))


# print(sorted(nx.get_edge_attributes(G, 'weight')))


# print communities within the graph (only 3 )
get_communities = True
if get_communities == True:
    find_communities = community.girvan_newman(G)
    top_level_communities = next(find_communities)
    next_level_communities = next(find_communities)
    communities = sorted(map(sorted, next_level_communities))
    print(communities)
