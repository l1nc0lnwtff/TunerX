import requests
import json
"""
https://de1.api.radio-browser.info/#List_of_radio_stations
https://de1.api.radio-browser.info/#List_of_countries
https://de1.api.radio-browser.info/#List_of_countrycodes
"""
"""
countryCode = "IL"
API_ENDPOINT = f"https://de1.api.radio-browser.info/json/stations/bycountrycodeexact/{countryCode}"
r = requests.get("http://de1.api.radio-browser.info/json/countries")
print(r.json())


TO DO:
sort stations by country , genre , votes
"""

def request(url:str) -> json:
    r = requests.get(url)
    return r.json()

def getJsonAttr(json:str, attr):
    return json[attr]
countries_json = request("http://all.api.radio-browser.info/json/countries")
indented = json.dumps(countries_json , indent=4)
ammount_of_countries = len(countries_json)
for i in range(0, ammount_of_countries): # we want to start the iteration from 0
    print(countries_json[i]["name"])
