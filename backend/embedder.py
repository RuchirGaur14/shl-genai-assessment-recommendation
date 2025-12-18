from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    cache_folder="./models"
)

def create_embeddings(df):
    """
    Create embeddings using name + description for better semantic separation.
    """
    texts = (df["name"] + " - " + df["description"]).tolist()
    embeddings = model.encode(texts)
    return np.asarray(embeddings, dtype="float32")
