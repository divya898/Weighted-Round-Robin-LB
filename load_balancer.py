import requests
import time
from random import choices

# Define the URLs of the servers and their corresponding weights
servers = [
    {"url": "http://54.174.5.92:8080/metrics", "weight": 1},
    {"url": "http://34.204.84.206:8080/metrics", "weight": 2}
]

def weighted_round_robin(servers):
    weights = [server["weight"] for server in servers]
    selected_server = choices(servers, weights=weights)[0]
    return selected_server["url"]

def fetch_data(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            print("Failed to fetch data from", url, "Status code:", r.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching data from", url, ":", e)
        return None

# Main loop
while True:
    selected_url = weighted_round_robin(servers)
    data = fetch_data(selected_url)
    if data:
        print(data)
    
    time.sleep(10) 