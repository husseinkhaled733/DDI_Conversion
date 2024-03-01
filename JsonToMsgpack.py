import msgpack
import json

# Load JSON data from file
with open("input.json", "r") as json_file:
    json_object = json.load(json_file)


print(json_object)

msgpack_file_path = "Msgpack_output.msgpack"
msgpack_data = msgpack.packb(json_object)

with open(msgpack_file_path, "wb") as msgpack_file:
    msgpack_file.write(msgpack_data)

print(f"Conversion complete. Msgpack data saved to '{msgpack_file_path}'.")
# Load Msgpack data from file
with open(msgpack_file_path, "rb") as msgpack_file:
    msgpack_data = msgpack.unpackb(msgpack_file.read())
    print(msgpack_data)
