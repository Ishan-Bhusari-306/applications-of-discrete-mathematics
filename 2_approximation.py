import networkx as nx
def approximation(g):
    N = g.number_of_nodes()
    MST = nx.minimum_spanning_tree(g);
    SC = list(nx.dfs_preorder_nodes(mstG, 0)); 
    W = sum([g[SC[i]][SC[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])
	weight = weight + g[sub_cycle[-1]][sub_cycle[0]]['weight']

    return weight
