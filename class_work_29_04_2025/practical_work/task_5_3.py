import requests

print("Reverse Geocoding with OpenStreetMap Nominatim API")
print("-------------------------------------------------")

def reverse_geocode(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        'lat': lat, 
        'lon': lon, 
        'format': 'json'
    }
    # Example
    # https://nominatim.openstreetmap.org/reverse?format=json&lat=12&lon=12
    headers = {
        'User-Agent': 'GeocoderApp'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None
        
        data = response.json()
        
        # Check for error response
        if 'error' in data:
            print(f"API Error: {data['error']}")
            return None
            
        # Check if we have meaningful data
        if not data.get('display_name'):
            print("No location found at these coordinates")
            return None
            
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Nominatim API: {e}")
        return None
    except ValueError:
        print("Error: Invalid response from API")
        return None

while True:
    try:
        lat = float(input("Enter latitude: "))
        lon = float(input("Enter longitude: "))

        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            print("Error: Valid ranges are -90 to 90 (lat) and -180 to 180 (lon)")
            continue
        break
    except ValueError:
        print("Error: Enter valid numeric values!\n")

data = reverse_geocode(lat, lon)

if data:
    print("\nReverse Geocoding Results:")
    print("--------------------------")
    print(f"Name: {data.get('name', 'N/A')}")
    print(f"Type: {data.get('type', 'N/A')}")
    print(f"Display Name: {data.get('display_name', 'N/A')}")
    
    print("\nAddress Details:")
    address = data.get("address", {})
    fields = {
        'house_number': 'House Number',
        'road': 'Street',
        'city': 'City',
        'town': 'Town', 
        'village': 'Village',
        'postcode': 'Postcode',
        'country': 'Country',
        'country_code': 'Country Code'
    }

    for field, label in fields.items():
        if field in address:
            value = address[field]
            if field == 'country_code':
                value = value.upper()
            print(f"{label}: {value}")
else:
    print("No results")
