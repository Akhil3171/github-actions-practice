import requests

API_URL = "https://api.open-meteo.com/v1/forecast"
LATITUDE = 17.3850
LONGITUDE = 78.4867


def fetch_temperature(latitude, longitude):
    """Fetch the current temperature in Celsius from the Open-Meteo API."""
    response = requests.get(
        API_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m",
        },
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    return data["current"]["time"], data["current"]["temperature_2m"]


def main():
    time, temp = fetch_temperature(LATITUDE, LONGITUDE)
    print(f"{time} -> {temp}°C")


if __name__ == "__main__":
    main()
