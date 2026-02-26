import requests
import pandas as pd

url = "https://api.odcloud.kr/api/15077586/v1/centers"
params = {
    "page": 1,
    "perPage": 5,
    "serviceKey": "YOUR_KEY"
}

res = requests.get(url, params=params)
df = pd.json_normalize(res.json())
print(df.head())
