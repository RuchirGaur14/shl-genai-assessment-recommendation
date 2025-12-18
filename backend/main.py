from fastapi import FastAPI
from pydantic import BaseModel
import os



from .data_loader import load_assessments
from .embedder import model, create_embeddings
from .search import build_faiss_index, search_assessments
from .metadata import enrich_metadata


app = FastAPI(title="SHL Assessment Recommendation API")


if not os.path.exists("data/shl_catalog.csv"):
    scrape_shl_catalog()

df = load_assessments()
embeddings = create_embeddings(df)
index = build_faiss_index(embeddings)


class QueryInput(BaseModel):
    query: str


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/recommend")
def recommend(data: QueryInput):
    
    query_vector = model.encode([data.query])

    
    results = search_assessments(query_vector, index, df)

    response = []
    seen = set()

    for item in results:
        if item["name"] in seen:
            continue
        seen.add(item["name"])

     
        metadata = enrich_metadata(item["name"])

        response.append({
            "assessment_name": item["name"],
            "assessment_url": item["url"],
            "test_type": metadata["test_type"],
            "duration": metadata["duration"],
            "remote_support": metadata["remote_support"],
            "adaptive_support": metadata["adaptive_support"]
        })

    return {"recommended_assessments": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
