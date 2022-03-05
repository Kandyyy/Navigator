import openrouteservice as ors
from geopy.geocoders import Nominatim
import folium
import webbrowser
from dotenv import load_dotenv
import os

#DECLARING API_KEY
load_dotenv('token.env')
ors_key = os.getenv('TOKEN')

#CLIENT
client = ors.Client(key=ors_key)

#Getting user start point
start_point = input("Enter startpoint: ")

#Getting user end point
end_point = input("Enter endpoint: ")

#Initializing obj
loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
getLoc1 = loc.geocode(start_point)
getLoc2 = loc.geocode(end_point)

coordinates = ((getLoc1.longitude, getLoc1.latitude), (getLoc2.longitude, getLoc2.latitude))
# directions
route = client.directions(coordinates=coordinates,profile='driving-car',format='geojson')

# map
map_directions = folium.Map(location=[getLoc1.latitude, getLoc1.longitude], zoom_start=18)

# add geojson to map
folium.GeoJson(route, name='route').add_to(map_directions)

# add layer control to map (allows layer to be turned on or off)
folium.LayerControl().add_to(map_directions)

# display map
map_directions.save("map.html")
webbrowser.open("map.html")
#map_directions

# distance and duration
print(route['features'][0]['properties']['segments'][0]['distance']*0.000621371*1.6, 'kms')
print(route['features'][0]['properties']['segments'][0]['duration']*0.000277778, 'hours\n')

# distances are in meters
# timings are in seconds
print('directions')
for index, i in enumerate(route['features'][0]['properties']['segments'][0]['steps']):
    print(index+1, i, '\n')
