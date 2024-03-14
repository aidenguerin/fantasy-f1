import requests
import json

def get_round_summary(round_number):
    r = requests.get(f"https://fantasy.formula1.com/feeds/drivers/{round_number}_en.json")
    return r.status_code, r.json()

def write_round_summary(path, json):
        with open(path, 'w') as f:
            json.dump(json, f)

ROUND_NUMBER = 1        
PATH = f"data/round_summary/{ROUND_NUMBER}.json"
status_code, data = get_round_summary(ROUND_NUMBER)

print(json.dumps(data, indent=4))

