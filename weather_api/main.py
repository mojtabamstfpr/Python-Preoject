import requests
API_KEY = "your_api_key"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
data = requests.get(url).json()
print(f"Weather in {city}: {data['weather'][0]['description']}")