# ingestion/test_api.py

import requests

url = "http://149.40.228.124:6500/records"

r = requests.get(url)

print(r.status_code)
print(r.text[:500])