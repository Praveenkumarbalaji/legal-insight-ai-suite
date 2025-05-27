import json
import pandas as pd

with open('data/fda/fda_enforcement.json', 'r') as f:
    data = json.load(f)

df = pd.json_normalize(data['results'])

def normalize_text(text):
    return text.lower().replace('\n', ' ').strip()

df['clean_description'] = df['product_description'].apply(normalize_text)
df.to_csv("data/fda/fda_enforcement_clean.csv", index=False)
