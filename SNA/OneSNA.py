Objective = """
Exercise 1
Write a Python program using the `networkx` to create and visualize an undirected graph with the following
specifications:
1. Create a graph with 5 nodes labeled `"A"`, `"B"`, `"C"`, `"D"`, and `"E"`.
2. Add the following edges between nodes:
 * "A" — "C"
 * "B" — "C"
 * "B" — "D"
 * "C" — "D"
 * "C" — "E"
 * "D" — "E"
3. Set the following 2D coordinates for each node:
 * A: (1, 5)
 * B: (4.5, 6.5)
 * C: (3.5, 1.4)
 * D: (5.8, 3.5)
 * E: (7.8, 3.8)
4. Visualize the graph with these style options:
 * Display node labels
 * Bold white font color for labels
 * Red-colored nodes with size 1000
 * Font size of 15
 * Edge width of 4

=========================================================================================================================================================================


"""
print(Objective)


# code begin from here


# importing python modules

import networkx as nx
import numpy as np


G=nx.Graph()
# Graph() init a empty graph
# G will be the graph
# the default graph should be undirected
# directed graph : G=nx.DiGraph()


G.add_node("A")
# this will create a node (vertices)
# labeled "A"
# label can be strings,number,tuples


G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")


# the vertices are ready
# now lets connect the vertices through edges
