import json
import requests
from bs4 import BeautifulSoup
import urllib


#variables
website_name = 'mudah'
mudah_domain = 'https://www.mudah.my/malaysia/mobile-phones-and-gadgets-for-sale?q=iPhone+13'

data = requests.get(mudah_domain)
html_content = data.text
soup = BeautifulSoup(html_content, "html.parser")

#data
link_script = soup.find_all("script", type="application/ld+json")
link_script_data = json.loads(link_script[0].get_text())

#for json data
raw_item_json = []

