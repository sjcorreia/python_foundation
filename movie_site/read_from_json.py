from __future__ import print_function
import json

with open('json/person.json') as json_data:
    # Reading from a JSON file into a python dict
    data = json.load(json_data)
    # It is important to know the structure of the data
    print(data["firstName"])
    print(data["address"]["streetAddress"])

    for key in data:
        print(key)

    print("=====")

    for key in data:
        print(data[key])
