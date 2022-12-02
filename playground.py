import json

with open("dietdata.json") as diets:
    j = json.load(diets)

print(len(j))
