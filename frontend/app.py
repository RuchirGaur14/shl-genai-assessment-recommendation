import streamlit as st
import requests

st.title("SHL Assessment Recommendation System")

query = st.text_area(
    "Enter job description or skill query",
    placeholder="e.g. Java developer with problem solving skills"
)

if st.button("Recommend"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/recommend",
                json={"query": query},
                timeout=30
            )

            if response.status_code == 200:
                st.subheader("Recommended Assessments")
                st.json(response.json())
            else:
                st.error(f"Backend error: {response.status_code}")
                st.text(response.text)

        except Exception as e:
            st.error(f"Could not connect to backend: {e}")
