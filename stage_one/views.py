from django.http import JsonResponse
import requests
from django.contrib.gis.geoip2 import GeoIP2

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location(request):

    g = GeoIP2(get_client_ip)
    log_lat = g.lon_lat()
    ip_address = get_client_ip(request)
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "lat_lat": log_lat
    }
    return JsonResponse(location_data)

# In your urls.py, you would then connect this view to a URL.
