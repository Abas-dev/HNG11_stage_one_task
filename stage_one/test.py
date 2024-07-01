import requests 

weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=6.4474&lon=3.3903&appid=0f7b64b6db127f0ed3e33e28639c5286")


print(weather.get("main"))