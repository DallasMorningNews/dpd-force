import json
import pprint
import csv


# the path we want to pull from. this should change based on the year of the data we want
filepath = "/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/force_orig-2014.json"

# year variable that is used to append to our outputted file
year = "2014"

# open the file
force_data = open(filepath).read()

# load the file as json
data = json.loads(force_data)

# set force_instances equal to the key we want to use in the force_data
force_instances = data["data"]

# setup and empty list to hold all our force objects
use_of_force = []

# populate our force objects
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

#append each of our force instance objects to the use_of_force list
    use_of_force.append(current_instance)

# open up the file we'll dump our data into
dpd_force_data = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/dpd_force_data-" + year + ".json", "w")

# dump our data
json.dump(use_of_force, dpd_force_data)

# close the file
dpd_force_data.close()

# create a new list that will hold the objects we have that don't have lat/long
no_geo = []

# iterate over our data, find the ones that don't have lat/long, and append it to the no_geo list
for item in use_of_force:
    if item["latitude"] == None:
        no_geo.append(item)

# set keys equal to the keys we'll need in our csv for the batch geocoding
keys = no_geo[0].keys()

# open a file that will hold our non-geo csv, write the keys, then write the actual data
with open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/no_geo-" + year + ".csv", "wb") as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(no_geo)
