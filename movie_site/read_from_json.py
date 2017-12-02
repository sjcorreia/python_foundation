from __future__ import print_function
import json

with open('json/person.json') as json_data:
    # Reading from a JSON file into a python dict
    data = json.load(json_data)
    # It is important to know the structure of the data
    
    print(data["firstName"])
    print(data["address"]["streetAddress"])

peopleList = []

with open('json/people.json') as json_data_people:
    # Reading from a JSON file into a python dict, or list of dicts
    data_people = json.load(json_data_people)
    # It is important to know the structure of the data

    for person in data_people:
        print(person["firstName"])
        peopleList.append(person["firstName"])
        # print(person["address"]["streetAddress"])

print(peopleList)
