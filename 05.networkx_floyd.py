# %%

import numpy as np
import networkx as nx

# %%

G = nx.DiGraph()
G.add_weighted_edges_from([
    ('v1', 'v2', 3),
    ('v1', 'v3', 2),
    ('v2', 'v4', 4),
    ('v2', 'v5', 6),
    ('v2', 'v6', 2),
    ('v3', 'v2', 8),
    ('v3', 'v4', 1),
    ('v3', 'v6', 3),
    ('v4', 'v5', 2),
    ('v6', 'v5', 5),
    ('v5', 'v7', 7),
    ('v6', 'v7', 3),
])

# %%

path = nx.shortest_path(G, weight='weight')
length = nx.shortest_path_length(G, weight='weight')
dict(path), dict(length)
