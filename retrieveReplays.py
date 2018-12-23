# Retrieves Maps from osu API
import requests
import json
import csv
import time

key = open('../../osu_api_key.txt', 'r').read()

parameters = {"k": key,
                "m": "3",
                "b": "1727102",
                "u": "JiEun"}        

response = requests.get("https://osu.ppy.sh/api/get_replay", params=parameters)
print(response.status_code) 

# Writes to json
with open('api_responses/replay_data/json/JiEun.json', 'w', encoding='utf-8') as outfile:
    json.dump(response.content.decode('utf-8'), outfile)


time.sleep(1) # Prevent spam requests