import requests
"""
https://de1.api.radio-browser.info/#List_of_radio_stations
https://de1.api.radio-browser.info/#List_of_countries
https://de1.api.radio-browser.info/#List_of_countrycodes
"""
countryCode = "IL"
API_ENDPOINT = f"https://de1.api.radio-browser.info/json/stations/bycountrycodeexact/{countryCode}"
r = requests.get("http://de1.api.radio-browser.info/json/countries")
print(r.json())