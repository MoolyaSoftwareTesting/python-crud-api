import json

def load_json(data):
    file_open = open(data)
    data = json.load(file_open)
    string = data['name'][0]['name'] + " " + data['name'][1]['name']
    return string


# Checking if my commit works V2.0.4
print(load_json(data="data.json"))
