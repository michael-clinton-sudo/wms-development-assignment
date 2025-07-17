
import requests
import os

NOCODB_API_URL = "https://api.nocodb.com"  # Replace with actual URL
API_KEY = "6y2v6LwaL2vTIkmvEFaLErpwDTDGgYCUStMCCz88"  # Replace with actual key
PROJECT = "InventoryDB"

def upload_to_nocodb(df):
    headers = {"xc-token": API_KEY, "Content-Type": "application/json"}
    for _, row in df.iterrows():
        record = row.to_dict()
        res = requests.post(f"{NOCODB_API_URL}/v1/db/data/noco/{PROJECT}/Shipments", json=record, headers=headers)
        print(res.status_code, res.text)
