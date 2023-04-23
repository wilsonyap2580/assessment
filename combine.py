import json
import pandas as pd


def run():
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

    #save sorted_combined_json into json file named: combined.json
    with open('combined.json','w') as file:
        file.write(json.dumps(sorted_combined_json))


    #save in text file
    with open('combined.txt','w') as file:
        for index, item in enumerate(sorted_combined_json):
            item_name = item['name']
            item_price = item['price']
            item_url = item['url']
            file.write(f'{index+1}. {item_name} - RM {item_price} - {item_url}\n') 


    #display in table format with pandas
    df = pd.DataFrame(sorted_combined_json)
    print(df.to_string())  