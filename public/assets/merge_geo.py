import json
import csv


force_data = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/dpd_force_data.json").read()

non_geo = json.loads(force_data)

with open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/no_geo2.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for line in reader:
        item_number = int(line["id"])

        for item in non_geo:
            if item["id"] == item_number:
                item["longitude"] = line["longitude"]
                item["latitude"] = line["latitude"]

dpd_force_geo = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/dpd_force_geo.json", "w")

json.dump(non_geo, dpd_force_geo)

dpd_force_geo.close()


# csvfile = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/no_geo2.csv", 'rb')
# Dictreader = csv.dictreader(csvfile)

# for item in non_geo:
#     item_number = item["id"]
#
#
#     for line in reader:
#         if item_number == line[3]:
#             item["longitude"] = line[2]
#             item["latitude"] = line[17]
#
# print non_geo
