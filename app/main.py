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
    return load_json(filename)


def load_txt(n_data, filename):
    with open(filename) as f:
        lines = f.readlines()
    with open(filename, "a") as update_txt:
        update_txt.write(f"firstname: {n_data['firstname']}\n")
        update_txt.write(f"lastname: {n_data['lastname']}\n")
        update_txt.write(f"mobile: {n_data['mobile']}\n")
        update_txt.write(f"email: {n_data['email']}\n \n")
    return lines


# V2.0.13
print(update_json(NEW_DATA, "data.json"))
print(load_txt(NEW_DATA, "text.txt"))
