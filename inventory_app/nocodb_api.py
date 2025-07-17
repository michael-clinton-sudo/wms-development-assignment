import requests
import os
import pandas as pd

# Configuration
NOCODB_API_URL = "https://api.nocodb.com"  # Replace with your actual NocoDB API URL
API_KEY = "6y2v6LwaL2vTIkmvEFaLErpwDTDGgYCUStMCCz88"  # Replace with your actual key
PROJECT = "InventoryDB"

def upload_to_nocodb(df):
    headers = {
        "xc-token": API_KEY,
        "Content-Type": "application/json"
    }

    # Convert Timestamps to string (ISO 8601 format)
    df = df.applymap(lambda x: x.isoformat() if isinstance(x, pd.Timestamp) else x)

    for _, row in df.iterrows():
        record = row.to_dict()
        try:
            res = requests.post(
                f"{NOCODB_API_URL}/v1/db/data/noco/{PROJECT}/Shipments",
                json=record,
                headers=headers
            )
            print(f"Status: {res.status_code}, Response: {res.text}")
        except Exception as e:
            print(f"Failed to upload record: {record}\nError: {e}")
