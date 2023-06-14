import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102199904%22%5D&companySize=%5B%22C%22%5D&industryCompanyVertical=%5B%221594%22%5D&origin=FACETED_SEARCH&sid=n2(")

if response.status_code == 200:    # successful request
    soup = BeautifulSoup(response.text, 'html.parser')

    compList = soup.findAll("a")
    compLocations = soup.findAll("div")

    print(len(compList))
    for comp in compList:
        print(comp)