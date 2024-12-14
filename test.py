from google.cloud import bigquery
import os

# Check if credentials are set
print(f"GOOGLE_APPLICATION_CREDENTIALS: {os.getenv('GOOGLE_APPLICATION_CREDENTIALS')}")

# Initialize BigQuery client
client = bigquery.Client()

# Test query
query = "SELECT COUNT(*) FROM `savvy-cinema-444321-g4.dsd_project_data.customer`"
query_job = client.query(query)  # Make an API request
results = query_job.result()  # Wait for the query to finish

for row in results:
    print(row)
