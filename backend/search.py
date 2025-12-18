import faiss
import numpy as np

def build_faiss_index(embeddings):
    """
    Build FAISS index for similarity search.
    """
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def search_assessments(query_embedding, index, df, top_k=10):
    """
    Retrieve top-K most relevant assessments.
    """
    query_embedding = np.asarray(query_embedding, dtype="float32")
    if query_embedding.ndim == 1:
        query_embedding = query_embedding.reshape(1, -1)

    _, indices = index.search(query_embedding, top_k)
    return df.iloc[indices[0]].to_dict("records")
