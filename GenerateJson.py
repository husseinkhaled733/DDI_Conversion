import json

# Load JSON data from file
with open("input.json", "r") as json_file:
    json_object = json.load(json_file)

print(json_object)

json_object_100 = {'entries': [json_object for _ in range(100)]}
with open("input_100.json", "w") as json_file:
    json.dump(json_object_100, json_file)
