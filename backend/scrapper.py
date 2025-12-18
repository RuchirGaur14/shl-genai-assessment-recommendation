import requests
import pandas as pd
import os

SHL_CATALOG_URL = "https://www.shl.com/solutions/products/product-catalog/"

def scrape_shl_catalog():
    """
    Demonstrates programmatic retrieval from SHL website.
    Since the catalog is dynamically rendered, we store
    catalog-level metadata to show the ingestion pipeline.
    """

    records = []

    try:
        response = requests.get(
            SHL_CATALOG_URL,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30
        )

        if response.status_code == 200:
            records.append({
                "name": "SHL Product Catalog (Dynamic)",
                "url": SHL_CATALOG_URL
            })

    except Exception as e:
        print("Error retrieving SHL catalog:", e)

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(records)
    df.to_csv("data/shl_catalog.csv", index=False)

    print(f"Stored {len(df)} SHL catalog records")
    return df


if __name__ == "__main__":
    scrape_shl_catalog()
