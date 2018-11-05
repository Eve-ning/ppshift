# Retrieves Maps from osu API
import requests
import json
import csv
import time

key = open('../../osu_api_key.txt', 'r').read()
ids = open('documents/Selected Maps.csv', 'r').read().split('\n')

for id in ids:
    parameters = {"k": key,
                 "b": id,
                 "m": "3",
                 "limit": "1"}        

    response = requests.get("https://osu.ppy.sh/api/get_scores", params=parameters)
    print(response.status_code)

    # Writes to json
    with open('api_responses/map_scores/json/' + id + '.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.content.decode('utf-8'), outfile)

    # Writes to csv
    with open('api_responses/map_scores/csv/' + id + '.csv', 'w', newline='') as respcsv:
        csv_file = csv.writer(respcsv)
        for score in json.loads(response.content):
            csv_file.writerow([score["score_id"],
                               score["score"],
                               score["username"],
                               score["count300"],
                               score["count100"],
                               score["count50"],
                               score["countmiss"],
                               score["maxcombo"],
                               score["enabled_mods"],
                               score["user_id"],
                               score["date"],
                               score["rank"],
                               score["pp"]]) 

    time.sleep(1) # Prevent spam requests