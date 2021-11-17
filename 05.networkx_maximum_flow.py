# %%

import numpy as np
import networkx as nx

# %%

G = nx.DiGraph()

edge_list = [
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
]

for edge in edge_list:
    G.add_edge(edge[0], edge[1], capacity=edge[2])

# %%

value, flow_dic = nx.maximum_flow(G, 'v1', 'v7')

# %%

value, flow_dic

# %%

dic = {}
for s in flow_dic:
    for t in flow_dic[s]:
        dic[(s,t)] = flow_dic[s][t]

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos)
nx.draw_networkx_edge_labels(T,pos=pos,
                             edge_labels=dic)
