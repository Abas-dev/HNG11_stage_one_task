from django.http import JsonResponse
import requests 
import os
from dotenv import load_dotenv

load_dotenv()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location(request):

    ip_address = get_client_ip(request)
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    lat = response.get("latitude")
    lon = response.get("longitude")

    API_key = os.getenv("API_key")

    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}")

    weather_data = weather.json()
    main_weather = weather_data.get('main')
    temp = main_weather.get('temp')

    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "lati": response.get("latitude"),
        "long": response.get("longitude"),
        "temp": temp
    }
    return JsonResponse(location_data)

# In your urls.py, you would then connect this view to a URL.
