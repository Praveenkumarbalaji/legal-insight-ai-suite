import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace

# Load cleaned FDA data
df = pd.read_csv("data/fda/fda_enforcement_clean.csv")
df = df.dropna(subset=["product_description", "classification", "reason_for_recall"])

# Initialize RDF graph and namespace
g = Graph()
FDA = Namespace("http://example.org/fda/")

# Convert rows into RDF triples
for _, row in df.iterrows():
    subject = URIRef(FDA[str(abs(hash(row["product_description"])))])
    recall_type = Literal(row["classification"])
    reason = Literal(row["reason_for_recall"])

    g.add((subject, FDA.hasRecallType, recall_type))
    g.add((subject, FDA.hasRecallReason, reason))

# Serialize outputs
g.serialize(destination="knowledge_graph/fda_recall_kg.ttl", format="turtle")
g.serialize(destination="knowledge_graph/fda_recall_kg.jsonld", format="json-ld")

print("✅ Knowledge Graph generated and saved as TTL & JSON-LD.")
