import json
file_open = open("data.json")
data = json.load(file_open)
string = ""


def load_json(data):
    global string
    string = data['name'][0]['name'] + " " + data['name'][1]['name']
    print(string)

# Checking if my commit works V2.0.3
load_json(data=data)