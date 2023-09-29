import json


def load_json(data):
    global return_data
    file_open = open(data)
    json_data = json.load(file_open)
    return_data = "Name: " + json_data['firstname'] + " " + json_data['lastname'] + ", " + "email: " + json_data[
        'email'] + ", " + "mobile: " + json_data['mobile']
    return return_data


# def update_json(jsonfile, data):
#     """input will be a dict and the file"""
#     """data is a dict"""
#     """jsonfile is a file"""

# V2.0.10
print(load_json("data.json"))
