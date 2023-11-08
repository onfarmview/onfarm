import folium
import pandas
import geemap.foliumap as geemap
map_center=(-43.525650, 172.639847)
Map = geemap.Map(
    basemap="HYBRID",
    plugin_Draw=True,
    Draw_export=True,
    locate_control=True,
    plugin_LatLngPopup=False, center=map_center, zoom=6.25,
)

bounds = Map.get_bounds()

popup_message = 'Contact: admin@onfarmview.com'+ str(bounds)
# folium.Marker(
#     location=map_center,
#     popup=popup_message,
#     icon=folium.Icon(color='blue')
# ).add_to(map)
marker = folium.Marker(
    location=map_center, #[bounds[0][2], bounds[1][3]],  # Use the top-right corner coordinates of the map
    popup=popup_message,
    icon=folium.Icon(icon="info-sign", color="red")
)
Map.add_child(marker)

Map.addLayerControl()
Map.save("index.html")
