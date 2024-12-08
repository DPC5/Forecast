from nws_api import fetch_nws_alerts, format_nws_alert
from map import map_alerts
import json

DATA_FILE_PATH = "data/nws_alerts.json"  

def save_json(data, output_file):

    if "@context" in data:
        del data["@context"]
    
    if "type" in data:
        del data["type"]
    if "features" in data:

        features_data = []
        for feature in data.get("features", []):
            features_data.append({
                "geometry": feature.get("geometry"),
                "properties": feature.get("properties")
            })
        data = features_data 

    # Save the modified JSON to the file
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def main():
 
    alerts_data = fetch_nws_alerts()

    #saving alerts to a json

    save_json(alerts_data, DATA_FILE_PATH)

    print(f"File saved to {DATA_FILE_PATH}")


if __name__ == "__main__":
    main()
