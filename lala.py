import json
with open("data.json") as f:
    data = json.load(f)

dar=data['ApartmentBuilding']['Apartments']
for apartment in dar:
    new=(apartment['Residents'])
    for i in new:
        print(i['Name'])