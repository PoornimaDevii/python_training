
import json

mycompounds = [{"name":"Fructose",
                "formula":"C6H1206",
                "id": 79025,
                "similarTo": ["Hexose", "Glucose"]}]
with open("samp_json.json","w") as jsonFile:
    json.dump(mycompounds, jsonFile)