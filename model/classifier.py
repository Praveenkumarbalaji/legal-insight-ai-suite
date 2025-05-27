import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
import joblib
import os

df = pd.read_csv("data/fda/fda_enforcement_clean.csv")
df = df[df['classification'].notna()]
X = df['clean_description']
y = df['classification']

vec = TfidfVectorizer()
X_vec = vec.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model and vectorizer
os.makedirs("model/artifacts", exist_ok=True)
joblib.dump(model, "model/artifacts/recall_model.joblib")
joblib.dump(vec, "model/artifacts/vectorizer.joblib")
