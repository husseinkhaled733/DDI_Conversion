from thrift.protocol import TJSONProtocol
from thrift.transport import TTransport
from menu import ttypes as menu_types
import json

# load JSON data from file
with open("input.json", "r") as json_file:
    json_object = json.load(json_file)

print(json_object)

menu = menu_types.Menu()
menu.header = json_object['menu']['header']
temp_list = []
for item in json_object['menu']['items']:
    menu_item = menu_types.MenuItem()
    if item is None:
        temp_list.append(menu_item)
        continue
    if "id" in item:
        menu_item.id = item['id']
    if "label" in item:
        menu_item.label = item['label']

    temp_list.append(menu_item)

menu.items = temp_list
transport = TTransport.TMemoryBuffer()
protocol = TJSONProtocol.TJSONProtocol(transport)
menu.write(protocol)

output_file_path = "Thrift_output.thrift"

with open(output_file_path, "w") as thrift_file:
    thrift_file.write(transport.getvalue().decode('utf-8'))






