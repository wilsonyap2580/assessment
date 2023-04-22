import json
import requests
from bs4 import BeautifulSoup
import urllib

#variables
website_name ='compasia'
compasia_domain = 'https://shop.compasia.com/a/search?q=iPhone+13'
data = requests.get(compasia_domain)

html_content = data.text
soup = BeautifulSoup(html_content, "html.parser")

#data found in class: product-item__info-inner
items = soup.find_all("div", {"class": "product-item__info-inner"})

#for json data
raw_item_json = []

#each item run for loop
for item in items:
    item_contents = item.contents 
    item_map = {}
    item_name = item_contents[1].get_text()
    item_map['name'] = item_name
    if item_contents[1].has_attr('href'):
        item_url = item_contents[1]['href']
        item_map['url'] = compasia_domain + item_url
    
    raw_item_price = item_contents[3].get_text()

    item_map['website_name'] = website_name
    item_map['price'] = raw_item_price
    
    # put all the json data into raw_item_json
    raw_item_json.append(item_map)

    # save raw_item_json into json file named: compasia.json
    with open('compasia.json', 'w')as file:
        file.write(json.dumps(raw_item_json))


