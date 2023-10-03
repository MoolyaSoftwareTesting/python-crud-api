import json


def load_json(data):
    file_open = open(data)
    json_data = json.load(file_open)
    update_json(json_data["data"][0])


def update_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["data"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


# V2.0.11
load_json("data.json")
