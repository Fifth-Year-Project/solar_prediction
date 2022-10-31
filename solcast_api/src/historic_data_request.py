import requests

key = "o2QrwWjwvAIaBQ4O4ZnfaHfT5dHXf34b"
url = f"https://api.solcast.com.au/world_radiation/estimated_actuals?latitude=56.187094&longitude=-3.962555&hours=168&api_key={key}"

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers, data=payload)
a=1