import requests
import json

def get_round_summary(round_number):
    r = requests.get(f"https://fantasy.formula1.com/feeds/drivers/{round_number}_en.json")
    return r.status_code, r.json()

def write_round_summary(path, json):
        with open(path, 'w') as f:
            json.dump(json, f)

def print_json(data):
    print(json.dumps(data, indent=4))

def get_asset_ids(round_summary):
    assets = data["Data"]["Value"]
    asset_ids = []
    for asset in assets:
        asset_ids.append(asset["PlayerId"])

    return asset_ids

def get_asset_stats(asset_id):
    r = requests.get(f"https://fantasy.formula1.com/feeds/popup/playerstats_{asset_id}.json")
    return r.status_code, r.json()

ROUND_NUMBER = 1        
PATH = f"data/round_summary/{ROUND_NUMBER}.json"
status_code, data = get_round_summary(ROUND_NUMBER)

status_code, data = get_asset_stats(210)
print_json(data)

