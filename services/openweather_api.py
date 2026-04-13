import requests
from datetime import datetime
def get_weather(city):

    API_KEY = "25fa0ac1297709dd40b79bbbb83f8f31" # Nie powinien być na widoku!

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        record = {
            "city": data.get("name"),
            "temp": data.get("main").get("temp"),
            "feels_like": data.get("main").get("feels_like"),
            "wind": data.get("wind").get("speed"),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return record
    except Exception as e:
        print(e)



