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

pos=nx.spring_layout(G, iterations=20)

nx.draw_networkx(G, pos=pos)
nx.draw_networkx_edge_labels(G,pos=pos,
                             edge_labels=nx.get_edge_attributes(G, 'weight'))

