# %%

import numpy as np
import networkx as nx

# %%

A = np.array([[0, 9, 2, 4, 7],
              [9, 0, 3, 4, 0],
              [2, 3, 0, 8, 4],
              [4, 4, 8, 0, 6],
              [7, 0, 4, 6, 0]])
G = nx.Graph(A)

# %%

T = nx.minimum_spanning_tree(G)

# %%

pos=nx.spring_layout(T, iterations=20)

nx.draw_networkx(T, pos=pos)
nx.draw_networkx_edge_labels(T,pos=pos,
                             edge_labels=nx.get_edge_attributes(T, 'weight'))