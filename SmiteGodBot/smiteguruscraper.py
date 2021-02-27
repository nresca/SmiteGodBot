import requests
from bs4 import BeautifulSoup

def scrapeData(playerurl):
    url = "https://smite.guru/profile/1472259-RiceyRice/casual"
    if playerurl != "":
        url = playerurl
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id= 'cw')
    data = results.find_all('div', True, class_ = 'percentile-stat__value c-help col-11')
    wlRatio = str(data[1].text).strip()
    return wlRatio.strip('%')

#print(scrapeEricData("abc"))