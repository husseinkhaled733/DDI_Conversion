from thrift.protocol import TJSONProtocol
from thrift.transport import TTransport
from menu import ttypes as menu_types
import json

# load JSON data from file
with open("input_100.json", "r") as json_file:
    json_object = json.load(json_file)

print(json_object)

repeated_menu = menu_types.repeatedMenu()
menu_list = []
for entry in json_object['entries']:
    menu = menu_types.Menu()
    menu.header = entry['menu']['header']
    temp_list = []
    for item in entry['menu']['items']:
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
    menu_list.append(menu)

repeated_menu.menus = menu_list
transport = TTransport.TMemoryBuffer()
protocol = TJSONProtocol.TJSONProtocol(transport)
repeated_menu.write(protocol)

output_file_path = "Thrift_output_100.thrift"

with open(output_file_path, "w") as thrift_file:
    thrift_file.write(transport.getvalue().decode('utf-8'))






