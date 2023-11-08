
import folium

# Create a map centered at a specific location
map = folium.Map(location=[latitude, longitude], zoom_start=12)

# Add a marker to the map
folium.Marker(
    location=[-43.64525717899288, 172.46137515298432],
    popup='Marker Popup Text'
).add_to(map)

# Save the map as an HTML file
map.save('map.html')
