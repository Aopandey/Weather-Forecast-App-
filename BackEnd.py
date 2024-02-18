import requests

API_KEY = "843f9cea82688b3fd6fa12fbba495fdf"


def get_data(city, day):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8 * day]
    return filtered_data
