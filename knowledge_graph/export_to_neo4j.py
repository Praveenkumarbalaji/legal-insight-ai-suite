import rdflib
import csv
import os

g = rdflib.Graph()
g.parse("knowledge_graph/fda_recall_kg.ttl", format="turtle")

os.makedirs("knowledge_graph/neo4j", exist_ok=True)

nodes = set()
edges = []

# Extract nodes and edges
for s, p, o in g:
    nodes.add(str(s))
    nodes.add(str(o))
    edges.append((str(s), str(p), str(o)))

# Write nodes.csv
with open("knowledge_graph/neo4j/nodes.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["id:ID"])
    for n in sorted(nodes):
        writer.writerow([n])

# Write edges.csv
with open("knowledge_graph/neo4j/edges.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow([":START_ID", ":TYPE", ":END_ID"])
    for start, rel, end in edges:
        rel_label = rel.split("/")[-1]  # use predicate name as edge type
        writer.writerow([start, rel_label, end])

print("✅ Export complete: nodes.csv and edges.csv ready for Neo4j import.")
