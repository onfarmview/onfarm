import folium
import pandas
import geemap.foliumap as geemap
import ee
from datetime import date, timedelta, datetime
def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
    geemap.ee_initialize(token_name=token_name)
def maskCloudAndShadows(image):
  cloudProb = image.select('MSK_CLDPRB')
  snowProb = image.select('MSK_SNWPRB')
  cloud = cloudProb.lt(5)
  snow = snowProb.lt(5)
  scl = image.select('SCL')
  shadow = scl.eq(3); # 3 = cloud shadow
  cirrus = scl.eq(10); # 10 = cirrus
  # Cloud probability less than 5% or cloud shadow classification
  mask = (cloud.And(snow)).And(cirrus.neq(1)).And(shadow.neq(1))
  return image.updateMask(mask).divide(10000)

ee_authenticate(token_name="4/1AfJohXkTlWMKd8fPevD3hd4tAq_j-YlD2CabTy7QtM7iu1gNB3XdBEqRehA")

map_center=(-43.525650, 172.639847)
popup_message = 'Contact: admin@onfarmview.com'
crs = "epsg:4326"
band = ['B8','B4','B3']
rgbViza = {"min":0.0, "max":0.7,"bands":band}

Map = geemap.Map(
    basemap="HYBRID",
    plugin_Draw=True,
    Draw_export=True,
    locate_control=True,
    plugin_LatLngPopup=False, center=map_center, zoom=6.25,
)

ed = date.today()
sd = ed - timedelta(days=30)


startDate = sd.strftime("%Y-%m-%d") + "T" 
endDate = ed.strftime("%Y-%m-%d") + "T"


se2 = ee.ImageCollection('COPERNICUS/S2_SR').filterDate(
            startDate,endDate).filter(
            ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE",90)).map(maskCloudAndShadows).median()


band = ['B4','B3','B2']
rgbViza = {"min":0.0, "max":0.7,"bands":band}
titlemap = "Sentinel 2 - Natural Color"
Map.addLayer(se2, rgbViza, titlemap)


band = ['B8','B4','B3']
rgbViza = {"min":0.0, "max":0.7,"bands":band}
titlemap = "Sentinel 2 - Color Infrared"
Map.addLayer(se2, rgbViza, titlemap)

band = ['B11','B8','B2']
rgbViza = {"min":0.0, "max":0.7,"bands":band}
titlemap = "Sentinel 2 - Agriculture"
Map.addLayer(se2, rgbViza, titlemap)

band = ['B11','B8','B4']
rgbViza = {"min":0.0, "max":0.7,"bands":band}
titlemap = "Sentinel 2 - Vegetation Analysis"
Map.addLayer(se2, rgbViza, titlemap)

band = ['B8','B11','B2']
rgbViza = {"min":0.0, "max":0.7,"bands":band}
titlemap = "Sentinel 2 - Healthy Vegetation"
Map.addLayer(se2, rgbViza, titlemap)


folium.Marker(
    location=map_center,
    popup=popup_message,
    icon=folium.Icon(icon="info-sign", color="red")
).add_to(Map)

Map.addLayerControl()
Map.save("index.html")
