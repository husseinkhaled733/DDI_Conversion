import menu_pb2
import json

# load JSON data from file
with open("input.json", "r") as json_file:
    json_object = json.load(json_file)

print(json_object)


menu = menu_pb2.Menu()
menu.header = json_object['menu']['header']
for item in json_object['menu']['items']:
    menu_item = menu.items.add()
    if item is None:
        continue
    if "id" in item:
        menu_item.id = item['id']
    if "label" in item:
        menu_item.label = item['label']

proto_file_path = "Proto_output.proto"
with open(proto_file_path, "wb") as proto_file:
    proto_file.write(menu.SerializeToString())
