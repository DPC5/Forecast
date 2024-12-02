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


def get_alerts():
    
    alerts_url = f'https://api.weather.gov/alerts/active/area/{code}'
    response = urlopen(alerts_url)
    data = json.load(response)

    # Sort through response and list out the location and description of the alert

    return ret







#TODO
# Most likey just use matplot lib to generate a percipitation map around the location of the user
# Ill keep the api key in there incase i need to use a different api which i prob will need to
# 