
import requests
import pandas as pd
import json

# Configuration
API_URL = "http://127.0.0.1:8000/api/admin/participants/"
TOKEN = "YOUR_ADMIN_TOKEN_HERE" # User needs to replace this

headers = {
    "Authorization": f"Token {TOKEN}"
}

try:
    print(f"Fetching data from {API_URL}...")
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if not data:
            print("No data found.")
        else:
            df = pd.DataFrame(data)
            output_file = "participants_export.csv"
            df.to_csv(output_file, index=False)
            print(f"Successfully exported {len(data)} records to {output_file}")
            print(df.head())
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")
