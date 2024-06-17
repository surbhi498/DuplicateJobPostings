import pandas as pd
from sentence_transformers import SentenceTransformer
import os
import torch

# Load data
data_path = "./data/jobpostings.csv"
df = pd.read_csv(data_path)
# Filter out rows with NA job descriptions
df = df.dropna(subset=['Job Description'])
print(f"Number of rows after dropping NaN: {len(df)}")

# Load your Sentence Transformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cpu')

# Generate embeddings and save to file
embeddings = model.encode(df['Job Description'].tolist(), convert_to_tensor=True, device='cpu')
embedding_file_path = "./embeddings/job_description_embeddings.pt"
torch.save(embeddings, embedding_file_path)
print(f"Embeddings saved to {embedding_file_path}")