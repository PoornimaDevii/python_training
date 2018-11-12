import json

with open('samp_json.json','r') as jsonFile:
    compounds = json.load(jsonFile)

print(compounds[0]["name"])
print(compounds[0]["similarTo"][0])
print(compounds[0]["similarTo"][1])
print(compounds[0]['formula'])
print(compounds[0]['id'])