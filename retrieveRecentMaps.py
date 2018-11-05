# Retrieves Maps from osu API
import requests
import json

key = open('../../osu_api_key.txt', 'r').read()

parameters = {"k": key,
             "since": "2018-06-30 11:00:12",
             "m": "3",
             "limit": "500"}

response = requests.get("https://osu.ppy.sh/api/get_beatmaps", params=parameters)
print(response.status_code)

with open('api_responses/response10.json', 'w', encoding='utf-8') as outfile:
    json.dump(response.content.decode('utf-8'), outfile)