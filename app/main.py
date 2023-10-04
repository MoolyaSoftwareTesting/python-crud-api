import json

NEW_DATA = {
    "firstname": "DS",
    "lastname": "S",
    "mobile": "99999999",
    "email": "email@GMAIL.com"
}


def load_json(data):
    with open(data, "r") as file:
        json_data = json.load(file)
    return json_data


def update_json(n_data, filename):
    data = load_json(filename)
    data['data'].append(n_data)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    with open(filename, "r") as updated_file:
        json_updated_file = json.load(updated_file)
        return json_updated_file


# V2.0.12
print(update_json(NEW_DATA, "data2.json"))
