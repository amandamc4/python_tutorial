import requests

APY_KEY = "5bceb2ccf863efe388fbeef1b64c1c73"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APY_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    #filter by forecast days (8 data points each day times 2 days
    filtered_data = filtered_data[:8*forecast_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))