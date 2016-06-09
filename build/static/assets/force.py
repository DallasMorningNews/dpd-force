import json
import pprint
import csv

force_data = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/force_orig.json").read()

data = json.loads(force_data)

force_instances = data["data"]

use_of_force = []

for instance in force_instances:

    current_instance = {
        "id": instance[0],
        "date": instance[10],
        "time": instance[11],
        "curren_badge_no": instance[12],
        "officer_sex": instance[13],
        "officer_race": instance[14],
        "hire_date": instance[15],
        "officer_injured": instance[16],
        "officer_condition": instance[17],
        "officer_hospital": instance[18],
        "service_type": instance[19],
        "uof_num": instance[20],
        "force_type": instance[21],
        "uof_reason": instance[22],
        "force_effective": instance[24],
        "citizen_number": instance[25],
        "citizen_race": instance[26],
        "citizen_sex": instance[27],
        "citizen_injured": instance[28],
        "citizen_condition": instance[29],
        "citizen_arrested": instance[30],
        "citizen_assesment": instance[31],
        "citizen_charge": instance[32],
        "street_address": instance[33],
        "latitude": instance[41][1],
        "longitude": instance[41][2],
        "city": "Dallas",
        "state": "TX",
        "zip": ""
    }

    use_of_force.append(current_instance)


dpd_force_data = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/dpd_force_data.json", "w")

json.dump(use_of_force, dpd_force_data)

dpd_force_data.close()

no_geo = []


for item in use_of_force:
    if item["latitude"] == None:
        no_geo.append(item)
        print item


print no_geo


keys = no_geo[0].keys()
with open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/no_geo.csv", "wb") as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(no_geo)

# dpd_no_geo = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/dpd_no_geo.json", "w")
#
# json.dump(no_geo, dpd_no_geo)
#
# dpd_no_geo.close()
