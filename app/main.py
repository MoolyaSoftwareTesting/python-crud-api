import json

def load_json(data):
    global return_data
    file_open = open(data)
    json_data = json.load(file_open)
    return json_data[0]


def update_json(new_data, file_name="data.json"):
    with open("data.json", 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


update_json(load_json("data.json"))
# V2.0.10
#print(load_json("data.json"))
