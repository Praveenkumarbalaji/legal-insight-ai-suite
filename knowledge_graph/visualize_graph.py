import rdflib
import networkx as nx
import matplotlib.pyplot as plt

# Load the RDF graph
g = rdflib.Graph()
g.parse("knowledge_graph/fda_recall_kg.ttl", format="turtle")

# Build a NetworkX graph (limit to first 100 triples for clarity)
G = nx.DiGraph()
for i, (s, p, o) in enumerate(g):
    if i >= 100:
        break
    G.add_edge(str(s), str(o), label=str(p))

# Draw the graph
plt.figure(figsize=(15, 12))
pos = nx.spring_layout(G, k=0.7, iterations=100)

nx.draw(G, pos, with_labels=False, node_size=30, node_color="skyblue", edge_color="gray", alpha=0.7)

# Optional: draw edge labels (uncomment to enable)
# edge_labels = nx.get_edge_attributes(G, 'label')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

plt.title("FDA Recall Knowledge Graph (Top 100 Triples)")
plt.tight_layout()
plt.savefig("knowledge_graph/fda_graph_visualization.png")
print("✅ Simplified graph saved to knowledge_graph/fda_graph_visualization.png")
