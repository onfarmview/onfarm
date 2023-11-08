import folium
import pandas
import geemap.foliumap as geemap
map_center=(-43.525650, 172.639847)
map = geemap.Map(
    basemap="HYBRID",
    plugin_Draw=True,
    Draw_export=True,
    locate_control=True,
    plugin_LatLngPopup=False, center=map_center, zoom=6.25,
)
popup_message = 'Contact: admin@onfarmview.com'
folium.Marker(
    location=map_center,
    popup=popup_message,
    icon=folium.Icon(color='blue')
).add_to(map)

map.addLayerControl()
map.save("index.html")
