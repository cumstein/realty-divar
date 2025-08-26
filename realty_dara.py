import requests
import json

API_KEY = "eyJhbGciOiJSUzI1NiIsImtpZCI6InByaXZhdGVfa2V5XzIiLCJ0eXAiOiJKV1QifQ.eyJhcHBfc2x1ZyI6InNob3J0LXBldGFsLXNhcmdlbnQiLCJhdWQiOiJzZXJ2aWNlcHJvdmlkZXJzIiwiZXhwIjoxNzYxMzIyMDczLCJqdGkiOiJhODIwZmFmOS04MWNkLTExZjAtYWYzMy0wMmExOTFjYzdkN2UiLCJpYXQiOjE3NTYxMzgwNzMsImlzcyI6ImRpdmFyIiwic3ViIjoiYXBpa2V5In0.mWoX3l3BcCv9O_uEWJfyN63OzUGDmOMlxpNCtZhAnufeakqt-sUz6riKZYBdNDDZ70HkEpWnPqOipJkXBEtP39_wSMKquSd7TII8pe_asgRFGQy-9OVHLJ3ZxbsDYRIgKnZkeyxmJUmgGqhha2esU-tOJULy1-MivCkRlnFukS7VHgXkHopXe_Ectxvn6wqLQ4Cl9HFkHMKkfTv3p8TjtwZBdYRDTvm4zzbs5yEpuZiua4mhVkkFKAyKcnE6MwCjLD9QWBknwBklmWQXiyVqwbp7jOpZknqRIS-xu1BUj5QB5WiugJNjyD7Kf6seMtCNyTYKFQQdM6D_nxBQKcgDZg"

url = "https://open-api.divar.ir/v2/open-platform/finder/post"

headers = {
    "Accept": "application/json",
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "category": "real-estate", 
    "city": "tehran",
    "districts": ["nazi-abad"],
}


response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("پاسخ موفقیت‌آمیز:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
else:
    print(f"خطا در درخواست: {response.status_code}")
    print(response.text)
