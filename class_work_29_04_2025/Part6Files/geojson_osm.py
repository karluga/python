import urllib.request, urllib.parse, urllib.error
import json
import ssl

# https://nominatim.openstreetmap.org/
# https://nominatim.org/

serviceurl = 'https://nominatim.openstreetmap.org/search?'
osm_format = 'geojson'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['q'] = address
    parms['format'] = osm_format
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lng = js['features'][0]['geometry']['coordinates'][0]
    lat = js['features'][0]['geometry']['coordinates'][1]
    print('lat', lat, 'lng', lng)
    location = js['features'][0]['properties']['display_name']
    print(location)
