ques = """

TASK : Plot rewiring of watts-stragatz model graph consider:
        N = 20
        K = 5
        p = 0,0.01,0.05,0.1,0.5,1.0

display no of nodes and edges
find : average clsutering coefficent , average shortest path length

"""


notes = """


"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

N = 1000
K = 10
p_values = [0, 0.01, 0.05, 0.1, 0.5, 1.0]
seed = 42

results = []

for p in p_values:
    G = nx.watts_strogatz_graph(n=N, k=K, p=p, seed=seed)

    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()

    avg_clust = nx.average_clustering(G)

    # average shortest path length (works only if connected)
    if nx.is_connected(G):
        avg_path = nx.average_shortest_path_length(G)
    else:
        # use largest connected component
        largest_cc = max(nx.connected_components(G), key=len)
        G_cc = G.subgraph(largest_cc).copy()
        avg_path = nx.average_shortest_path_length(G_cc)

    results.append({
        'p': p,
        'nodes': n_nodes,
        'edges': n_edges,
        'avg_clustering': avg_clust,
        'avg_path': avg_path
    })

    print(f"p = {p:<5} | nodes = {n_nodes} | edges = {n_edges} "
          f"| avg clustering = {avg_clust:.4f} | avg shortest path = {avg_path:.4f}")

# Put into arrays for plotting
ps = [r['p'] for r in results]
clusts = [r['avg_clustering'] for r in results]
paths = [r['avg_path'] for r in results]

# ---- Plot 1: metrics vs p ----
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(ps, clusts, marker='o', color='steelblue')
axes[0].set_xlabel('rewiring probability p')
axes[0].set_ylabel('average clustering coefficient')
axes[0].set_title('Clustering vs p')
axes[0].grid(True, alpha=0.3)

axes[1].plot(ps, paths, marker='s', color='crimson')
axes[1].set_xlabel('rewiring probability p')
axes[1].set_ylabel('average shortest path length')
axes[1].set_title('Path length vs p')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ws_metrics.png', dpi=150)
plt.show()

# ---- Plot 2: the graphs themselves (smaller N for visibility) ----
N_small = 50
K_small = 4
p_small = [0, 0.01, 0.05, 0.1, 0.5, 1.0]

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
for ax, p in zip(axes.ravel(), p_small):
    G = nx.watts_strogatz_graph(n=N_small, k=K_small, p=p, seed=seed)
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=40, node_color='steelblue')
    nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.4)
    ax.set_title(f'N={N_small}, K={K_small}, p={p}')
    ax.axis('off')

plt.suptitle('Watts–Strogatz rewiring (small example for visibility)', y=1.02)
plt.tight_layout()
plt.savefig('ws_graphs.png', dpi=150)
plt.show()
