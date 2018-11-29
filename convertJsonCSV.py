# Converts JSON to CSV
import json
import csv

with open('api_responses/out.csv', 'w', newline='') as respcsv:
    csv_file = csv.writer(respcsv)

    for x in range(0, 11):
        with open('api_responses/response' + str(x) + '.json', encoding='utf-8') as resp:
            respJson = json.loads(json.load(resp))

        for map in respJson:
            csv_file.writerow([map["approved_date"],
                               map["beatmap_id"],
                               map["beatmapset_id"],
                               map["difficultyrating"],
                               map["diff_size"],
                               map["hit_length"],
                               map["favourite_count"],
                               map["playcount"],
                               map["passcount"],
                               map["artist"],
                               map["title"],
                               map["version"]])
