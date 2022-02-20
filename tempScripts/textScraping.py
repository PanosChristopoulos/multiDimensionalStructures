import requests
from bs4 import BeautifulSoup
import json



import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "generator": "random",
    "grnnamespace" : "0",
    "grnlimit": "3",
    "prop" : "info|extracts",
    "inprop" : "url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()['query']['pages']

urlList = []

for key,value in DATA.items():
     urlList.append(value['fullurl'])

for url in urlList:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find(id="firstHeading").get_text()
    print(title)
    """
    for data in soup.find_all("p"): 
        print(data.get_text()) 
    """
    article = soup.find("div", {"id":"bodyContent"}).findAll('p')
