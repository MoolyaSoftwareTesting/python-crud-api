import json

def load_json(data):
    file_open = open(data)
    json_data = json.load(file_open)
    string = json_data['name'][0]['name'] + " " + json_data['name'][1]['name']
    return string


#2.0.6
print(load_json("data.json"))