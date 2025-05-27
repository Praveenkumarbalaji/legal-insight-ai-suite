import streamlit as st
import pandas as pd

st.title("FDA Recall Insights")

# Load cleaned data with corrected path
df = pd.read_csv("data/fda/fda_enforcement_clean.csv")

st.write("### Sample Data")
st.dataframe(df.head())

st.write("### Classification Count")
st.bar_chart(df['classification'].value_counts())
