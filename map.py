import requests
import folium
from folium.plugins import HeatMap
import json

DATA_FILE_PATH = "data/nws_alerts.json"  

# Function to fetch coordinates from affected zones
def fetch_zone_coordinates(affected_zones):
    coordinates_list = []
    for zone_url in affected_zones:
        try:
            response = requests.get(zone_url)
            response.raise_for_status()
            zone_data = response.json()
            geometry = zone_data.get("geometry", {})
            if geometry and geometry["type"] == "Polygon":
                coordinates = geometry["coordinates"][0]  
                coordinates_list.append(coordinates)
        except requests.RequestException as e:
            print(f"Error fetching zone data from {zone_url}: {e}")
    return coordinates_list



# Function to map alerts

def get_alert_color(alert_type):

    """
    Colors alerts based on what they are
    """

    if alert_type.find("Warning") != -1:
        return "red"
    elif alert_type.find("Watch") != -1:
        return "orange"
    elif alert_type.find("Advisory") != -1:
        return "yellow"
    elif alert_type.find("Special") != -1:
        return "white"
    else:
        return "grey"  

import folium

def map_alerts(alerts, map_file="nws_alert_map.html"):

    """
    This maps out the alerts using folium
    """

    us_map = folium.Map(location=[37.8, -96], zoom_start=4)  

    for alert in alerts:
        alert_type = alert["properties"].get("event", "Unknown")  
        affected_zones = alert["properties"].get("affectedZones", [])
        coordinates_list = fetch_zone_coordinates(affected_zones)

        color = get_alert_color(alert_type)

        for coordinates in coordinates_list:

            polygon = folium.Polygon(
                locations=[[lat, lon] for lon, lat in coordinates], 
                color=color,
                weight=2,
                fill=True,
                fill_color=color,
                fill_opacity=0.5,
            )

            name = alert["properties"].get("headline", "No Name")
            description = alert["properties"].get("description", "No Description")


            tooltip_text = f"<b>{name}</b>"
            tooltip = folium.Tooltip(tooltip_text)
            polygon.add_child(tooltip)

            popup_text = f"<b>{name}</b><br>{description}"
            popup = folium.Popup(popup_text, max_width=300)
            polygon.add_child(popup)

            polygon.add_to(us_map)

    us_map.save(map_file)
    print(f"Map has been saved as '{map_file}'")




with open(DATA_FILE_PATH, 'r') as f:
    data = json.load(f)

map_alerts(data)
