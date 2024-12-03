from nws_api import fetch_nws_alerts, format_nws_alert


def main():
 
    alerts_data = fetch_nws_alerts()

    formatted = format_nws_alert(alerts_data)

    print(formatted)

if __name__ == "__main__":
    main()
