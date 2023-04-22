import json
import pandas as pd

#create empty list
combined_json = []

#read mudah json
with open('mudah.json', 'r') as file:
    mudah_json = json.loads(file.read())
    combined_json.extend(mudah_json)

#read compasia json
with open('compasia.json', 'r') as file:
    compasia_json = json.loads(file.read())
    combined_json.extend(compasia_json)


#sort price in ascending order
sorted_combined_json = sorted(combined_json, key=lambda k: k['price'], reverse=False)
