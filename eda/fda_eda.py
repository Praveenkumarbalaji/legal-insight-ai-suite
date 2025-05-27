import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/fda/fda_enforcement_clean.csv')

# Fix date parsing: ensure column exists and is valid
if 'recall_initiation_date' in df.columns:
    df['recall_initiation_date'] = pd.to_datetime(df['recall_initiation_date'], format='%Y%m%d', errors='coerce')
    df = df[df['recall_initiation_date'].notna()]
    df['year'] = df['recall_initiation_date'].dt.year
    df['year'].value_counts().sort_index().plot(kind='bar', title="Recalls Per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Recalls")
    plt.tight_layout()
    plt.savefig("eda/recalls_per_year.png")
else:
    print("recall_initiation_date column is missing.")
