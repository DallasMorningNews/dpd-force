import json
import csv

json_file_path = "/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/dpd_force_data-2014.json"
csv_file_path = "/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/geo-added-2014.csv"
year = "2014"

force_data = open(json_file_path).read()

non_geo = json.loads(force_data)

with open(csv_file_path) as csvfile:
    reader = csv.DictReader(csvfile)

    for line in reader:
        item_number = int(line["id"])

        for item in non_geo:
            if item["id"] == item_number:
                item["longitude"] = line["longitude"]
                item["latitude"] = line["latitude"]

dpd_force_geo = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/dpd_force_geo-" + year + ".json", "w")

json.dump(non_geo, dpd_force_geo)

dpd_force_geo.close()
