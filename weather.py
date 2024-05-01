"""Fetch the current weather for a given latitude and longitude."""

import httpx
from prefect import flow


@flow(log_prints=True)
def fetch_weather(lat: float = 38.9, lon: float = -77.0):
    """Fetch the current weather for a given latitude and longitude."""
    base_url = "https://api.open-meteo.com/v1/forecast/"
    temps = httpx.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    forecasted_temp = float(temps.json()["hourly"]["temperature_2m"][0])
    print(f"Forecasted temp C: {forecasted_temp} degrees")
    return forecasted_temp


if __name__ == "__main__":
    fetch_weather.serve(
        name="pacc-2024-v2-101-weather1-serve",
        cron="* * * * *",
        parameters={"lat": 40.142368, "lon": -105.166733},
    )
