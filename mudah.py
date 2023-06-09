import json
import requests
from bs4 import BeautifulSoup

website_name = 'mudah'
def run():
    #variables
    
    mudah_domain = 'https://www.mudah.my/malaysia/mobile-phones-and-gadgets-for-sale?q=iPhone+13'

    data = requests.get(mudah_domain)
    html_content = data.text
    soup = BeautifulSoup(html_content, "html.parser")

    #data
    link_script = soup.find_all("script", type="application/ld+json")
    link_script_data = json.loads(link_script[0].get_text())

    #for json data ##
    jsondata = []

    for data in link_script_data[2]['itemListElement']:
        item_map = {}
        #check if dictionary contain item key
        if 'item' in data:
            item_url = data['item']['url']
            item_name = data['item']['name']
            # check if dictionary contain offers key
            if 'offers' in data['item']:
                item_price = data['item']['offers']['price']
                #convert to float
                item_price = float(item_price)
                item_map['price'] = item_price
            item_map['website_name'] = website_name
            item_map['name'] = item_name
            item_map['url'] = item_url
            
        # put all the json data into raw_item_json
        jsondata.append(item_map)

    with open('mudah.json', 'w') as file:
        file.write(json.dumps(jsondata))