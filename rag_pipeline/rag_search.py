import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned recall descriptions
df = pd.read_csv("data/fda/fda_enforcement_clean.csv")
corpus = df['clean_description'].dropna().tolist()

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
corpus_embeddings = model.encode(corpus, convert_to_tensor=True).cpu().numpy()

# User query
query = "pain relief medicine recall"
query_embedding = model.encode([query], convert_to_tensor=True).cpu().numpy()

# Calculate cosine similarity
scores = cosine_similarity(query_embedding, corpus_embeddings)[0]
top_idx = scores.argmax()
top_match = df.iloc[top_idx]

# Print result
print("🔍 Most Relevant Match for Query:")
print(top_match[['product_description', 'classification', 'recall_number', 'reason_for_recall']])
