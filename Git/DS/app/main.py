import json
import sys

file_name = sys.argv[1]
file_open = open(f'{file_name}')

data = json.load(file_open)


string = ""

data_2 = []

for i in data['name']:
    for j in dict.values(i):
        string = string + j

print(string)