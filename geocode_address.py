from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

def get_lat_lon_from_address(address):
    geolocator = Nominatim(user_agent="YourAppName_or_YourName")
    retries = 3 

    for attempt in range(retries):
        try:
            location = geolocator.geocode(address, timeout=10) 
            if location:
                return location.latitude, location.longitude
            else:
                print(f"Couldn't retrieve latitude and longitude for the provided address on attempt {attempt + 1}.")
                return None, None
        except GeocoderTimedOut:
            print(f"Timeout occurred on attempt {attempt + 1}. Retrying in 5 seconds...")
            time.sleep(5)
    print("Max retries reached. Couldn't retrieve latitude and longitude for the provided address.")
    return None, None

address = input("Enter the address: ")
lat, lon = get_lat_lon_from_address(address)
if lat and lon:
    print(f"Latitude: {lat}, Longitude: {lon}")
