import fastavro
import json

# Load JSON data from file
with open("input.json", "r") as json_file:
    json_object = json.load(json_file)


print(json_object)

avro_schema = {
    "type": "record",
    "name": "Menu",
    "fields": [
        {
            "name": "menu",
            "type": {
                "type": "record",
                "name": "MenuItem",
                "fields": [
                    {"name": "header", "type": "string"},
                    {
                        "name": "items",
                        "type": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "record",
                                    "name": "MenuEntry",
                                    "fields": [
                                        {"name": "id", "type": "string"},
                                        {"name": "label", "type": ["string", "null"]}
                                    ]
                                },
                                "null"
                            ]
                        }
                    }
                ]
            }
        }
    ]
}

parsed_schema = fastavro.parse_schema(avro_schema)

avro_file_path = "Avro_output.avro"

with open(avro_file_path, "wb") as avro_file:
    fastavro.writer(avro_file, parsed_schema, [json_object])