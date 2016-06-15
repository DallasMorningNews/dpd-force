import json
import pprint

dpd_force_geo_json = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/dpd_force_geo.json").read()

force_geo_data = json.loads(dpd_force_geo_json)

incidents = {}
count = 0
for incident in force_geo_data:
    if incident["time"] == None:
        incident["time"] = "No time given"

    incident_name = (incident["time"] + " " + incident["date"] + " " + incident["street_address"])

    if incident_name not in incidents:
        incidents[incident_name] = {}
        incidents[incident_name]["id"] = count
        incidents[incident_name]["address"] = incident["street_address"]
        incidents[incident_name]["date"] = incident["date"]
        incidents[incident_name]["latitude"] = incident["latitude"]
        incidents[incident_name]["longitude"] = incident["longitude"]
        incidents[incident_name]["time"] = incident["time"]
        incidents[incident_name]["force_use"] = [{"current_badge_no": incident["curren_badge_no"], "officer_sex": incident["officer_sex"], "officer_race": incident["officer_race"], "hire_date": incident["hire_date"], "officer_injured": incident["officer_injured"], "officer_hospital": incident["officer_hospital"], "service_type": incident["service_type"], "uof_num": incident["uof_num"], "force_type": incident["force_type"], "uof_reason": incident["uof_reason"], "force_effective": incident["force_effective"], "citizen_number": incident["citizen_number"], "citizen_race": incident["citizen_race"], "citizen_sex": incident["citizen_sex"], "citizen_injured": incident["citizen_injured"], "citizen_condition": incident["citizen_condition"], "citizen_arrested": incident["citizen_arrested"], "citizen_assesment": incident["citizen_assesment"], "citizen_charge": incident["citizen_charge"]}]

        count += 1
    else:
        incidents[incident_name]["force_use"].append({"current_badge_no": incident["curren_badge_no"], "officer_sex": incident["officer_sex"], "officer_race": incident["officer_race"], "hire_date": incident["hire_date"], "officer_injured": incident["officer_injured"], "officer_hospital": incident["officer_hospital"], "service_type": incident["service_type"], "uof_num": incident["uof_num"], "force_type": incident["force_type"], "uof_reason": incident["uof_reason"], "force_effective": incident["force_effective"], "citizen_number": incident["citizen_number"], "citizen_race": incident["citizen_race"], "citizen_sex": incident["citizen_sex"], "citizen_injured": incident["citizen_injured"], "citizen_condition": incident["citizen_condition"], "citizen_arrested": incident["citizen_arrested"], "citizen_assesment": incident["citizen_assesment"], "citizen_charge": incident["citizen_charge"]})


incidents = list(incidents.values())

map_data = open("/Users/johnhancock/Desktop/interactives/working/dpd-force/build/static/assets/map_data.json", "w")

json.dump(incidents, map_data)

map_data.close()
