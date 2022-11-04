import requests

key = "o2QrwWjwvAIaBQ4O4ZnfaHfT5dHXf34b"
#url = f"https://api.solcast.com.au/data/live/radiation_and_weather?latitude=-33.856784&longitude=151.215297&output_parameters=air_temp,dni,ghi&api_key={key}"
#url = f"https://api.solcast.com.au/data/forecast/radiation_and_weather?latitude=-33.856784&longitude=151.215297&output_parameters=air_temp,dni,ghi&format=json&api_key={key}"
url = f"https://api.solcast.com.au/world_radiation/estimated_actuals?latitude=-33.856784&longitude=151.215297&hours=168&api_key={key}"

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)

a=1

