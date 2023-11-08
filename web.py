import folium
import pandas
import geemap.foliumap as geemap

data = pandas.read_csv("volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano information:</h4>
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def pickcolor(elevation):
    '''
    Picks a color for the volcano marker depending on the altitude
    '''
    if elevation<1000:
        return "green"
    elif elevation<2000 and elevation>1000:
        return "orange"
    else:
        return "red"

# map = geemap.Map(location=[-43.64544350688903, 172.46472254972872], zoom_start = 6, basemap="HYBRID",)

# fg = folium.FeatureGroup(name="My Map")

# fg.add_child(folium.GeoJson(data=open('world1.json','r', encoding='utf-8-sig').read(),
# style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000
# else 'orange' if 1000000<= x['properties']['POP2005'] <2000000
# else 'yellow' if 2000000<= x['properties']['POP2005'] <3000000
# else 'red' }))

# for lt, ln, el, name in zip(lat, lon, elev, name):
#     iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
#     fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 8 , popup=folium.Popup(iframe),
#     fill_color = pickcolor(el), color = 'grey' , fill_opacity = 0.7))
map = geemap.Map(
    basemap="HYBRID",
    plugin_Draw=True,
    Draw_export=True,
    # locate_control=True,
    plugin_LatLngPopup=False, center=(-43.525650, 172.639847), zoom=6.25,
)


# map.add_child(fg)

map.save("index.html")
