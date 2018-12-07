import numpy as np
import networkx as nx
from networkx.algorithms import community #use community algorithm to detec communities within a graph



FielName="email-Eu-core-temporal.txt"
Graphtype=nx.DiGraph()   # use net.Graph() for undirected graph

# How to read from a file. Note: if your egde weights are int, change float to int.
G = nx.read_edgelist(FielName, create_using=Graphtype, nodetype=int, data=(('weight',float),))

get_nodes = False
if get_nodes == True:
    # Find the total number of degree, in_degree and out_degree for each node
    for x in G.nodes():
          print ("Node: ", x, " has total #degree: ",G.degree(x), " , In_degree: ", G.out_degree(x)," and out_degree: ", G.in_degree(x))

get_edges = False
if get_edges == True:
    # Find the weight for each node
    for u,v in G.edges():
          print ("Weight of Edge ("+str(u)+","+str(v)+")", G.get_edge_data(u,v))



print(sorted(nx.get_edge_attributes(G, 'weight')))




# print communities within the graph (only 3 )
get_communities = False
if get_communities == True:
    find_communities = community.girvan_newman(G)
    top_level_communities = next(find_communities)
    next_level_communities = next(find_communities)
    print(sorted(map(sorted, next_level_communities)))
