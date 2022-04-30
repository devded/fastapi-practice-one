import json

f = open("data.json")

data = json.load(f)

print(data)

def get_json_data():
    f = open("data.json")
    data = json.load(f)
    return data