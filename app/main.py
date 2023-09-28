import json


def load_json(data):
    global return_data
    file_open = open(data)
    json_data = json.load(file_open)
    return_data = "Name: " + json_data['firstname'] + " " + json_data['lastname'] + ", "+ "email: " + json_data['email'] + ", " + "mobile: " +json_data['mobile']
    return return_data

#V2.0.9
print(load_json("data.json"))