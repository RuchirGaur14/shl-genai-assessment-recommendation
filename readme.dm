SHL GenAI Assessment Recommendation System
Objective

Build a GenAI-based system that recommends relevant SHL assessments based on a job description or skill query using semantic retrieval.

Approach

1.The provided SHL dataset is used as the data ingestion source.

2.Assessment information is parsed and structured for retrieval.

3.Text embeddings are generated using a transformer model.

4.FAISS is used for efficient vector similarity search.

5.A rule-based enrichment layer infers assessment metadata.

6.A FastAPI backend exposes the required API endpoints.

API Endpoints
Health Check

GET /health
 
Recommendation

POST /recommend

Request

{ "query": "java development" }

Response

{
  "recommended_assessments": [
    {
      "assessment_name": "...",
      "assessment_url": "...",
      "test_type": "...",
      "duration": "...",
      "remote_support": "...",
      "adaptive_support": "..."
    }
  ]
}

How to Run

Install Dependencies

pip3 install -r requirements.txt

Run Backend

python3 -m backend.main

API will be available at:

http://127.0.0.1:8000

Run Frontend

streamlit run frontend/app.py

