import requests 
import json
from urllib.request import urlopen



#getting location
ip_url = 'http://ipinfo.io/json'
response = urlopen(ip_url)
data = json.load(response)

try:
    city = data['city']
    country = data['country']
    region = data['region']
    code = f'{region.split(" ")[0][0]+region.split(" ")[1][0]}'
except:
    city = "Buffalo" #Setting default location if nothing is found
    country = "US"
    region = "New York"
    code = "NY"

#location set done


def fetch_nws_alerts():

    url = "https://api.weather.gov/alerts/active"
    response = requests.get(url)
    response.raise_for_status()  
    return response.json()


#TODO
# Most likey just use matplot lib to generate a percipitation map around the location of the user
# Ill keep the api key in there incase i need to use a different api which i prob will need to
# 