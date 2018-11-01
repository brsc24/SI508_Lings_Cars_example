from advanced_expiry_caching import *
import requests
import json
from bs4 import BeautifulSoup 

CACHE_FNAME = "sample_cache.json"
url_to_scrape = "https://www.lingscars.com/"
primary_cache = Cache(CACHE_FNAME)

while primary_cache.get(url_to_scrape) is None: # Just one way of handling this, not the only option! 
	data = requests.get(url_to_scrape)
	html_text = data.text
	primary_cache.set(url_to_scrape,html_text,7) 

if primary_cache.get("https://www.lingscars.com/personal-car-leasing") is None:
	data = requests.get("https://www.lingscars.com/personal-car-leasing")
	htmltext = data.text 
	primary_cache.set("https://www.lingscars.com/personal-car-leasing",html_text,7)

## All pages cached -- no crawling ^

soup = BeautifulSoup(primary_cache.get(url_to_scrape),features="html.parser")
page_title = soup.find("title").text
# print(title)

nav = soup.find("nav",{"id":"navigation"})
# print(nav)

# Now can find and find_all inside it!

menu_maybe = nav.find_all("a")
print(menu_maybe[0].prettify())
for elem in menu_maybe:
	if elem.text != "X" and elem['href'] == "#": # specifications
		print(elem.text)



