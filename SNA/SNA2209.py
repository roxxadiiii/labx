ques = """

TASK : Plot and Observe different centralities for G(n,p) random graph:
        consider;
            n = 10
            p = 0,0.1,0.25,0.5,0.75,1.0

"""


notes = """


"""


# importing libs
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# taking given values
n = 10
p_values = [0,0.1,0.25,0.5,0.75,1.0]
seed = 42

centrality_funcs = {
    'degree': lambda G: nx.degree_centrality(G),
    'closeness': lambda G: nx.closeness_centrality(G),
    'betweenness': lambda G: nx.betweenness_centrality(G, normalized=True),
    'eigenvector': lambda G: nx.eigenvector_centrality(G, max_iter=1000, tol=1e-6)
}

results = {c: {} for c in centrality_funcs}
graphs = {}

for p in p_values:
    G = nx.gnp_random_graph(n, p, seed=seed)
    graphs[p] = G

    for c, func in centrality_funcs.items():
        try:
            vals = func(G)
        except nx.PowerIterationFailedConvergence:
            vals = {node: np.nan for node in G.nodes()}

        # ensure all nodes 0..9 appear
        results[c][p] = {node: vals.get(node, 0.0) for node in range(n)}


# Print mean table
print("Mean centrality (averaged over nodes):")
print("p\tdegree\tcloseness\tbetweenness\teigenvector")
for p in p_values:
    row = [np.mean(list(results[c][p].values())) for c in centrality_funcs]
    print(f"{p}\t" + "\t".join(f"{v:.3f}" for v in row))


# Plot 1: small multiples
fig, axes = plt.subplots(
    len(centrality_funcs), len(p_values),
    figsize=(18, 10), sharey='row'
)


for i, c in enumerate(centrality_funcs):
    for j, p in enumerate(p_values):
        ax = axes[i, j]
        vals = [results[c][p][node] for node in range(n)]
        ax.bar(range(n), vals, color='steelblue')
        ax.set_xticks(range(n))
        if i == 0:
            ax.set_title(f'p = {p}')
        if j == 0:
            ax.set_ylabel(c)
        if i == len(centrality_funcs) - 1:
            ax.set_xlabel('node')

plt.suptitle(f'Centralities for G(n,p), n={n}, seed={seed}', y=1.02)
plt.tight_layout()
plt.savefig('centralities_gnp_small_multiples.png', dpi=150)
plt.show()


# Plot 2: mean ± std vs p
fig2, axes2 = plt.subplots(2, 2, figsize=(10, 8))
for ax, c in zip(axes2.ravel(), centrality_funcs):
    means = [np.mean(list(results[c][p].values())) for p in p_values]
    stds = [np.std(list(results[c][p].values())) for p in p_values]
    ax.errorbar(p_values, means, yerr=stds, marker='o', capsize=5)
    ax.set_title(c)
    ax.set_xlabel('p')
    ax.set_ylabel('mean ± std')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('centralities_gnp_mean_std.png', dpi=150)
plt.show()
