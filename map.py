import folium
import pandas as pd
import requests
import json
import os



regions_data_csv = os.path.join("data", "regions.csv")
regions_geo = os.path.join("data", "swedish_provinces.geojson")
regions = pd.read_csv(regions_data_csv)
region_geo_json = pd.read_json(regions_geo)

m = folium.Map(location=[63.0054, 16.8801], zoom_start=5    )

# for features in region_geo_json["features"]:
#     for property_name, property_value in features["properties"].items():
#         print(property_name, property_value)

        
folium.Choropleth(
    geo_data=regions_geo,
    name='choropleth',
    data=regions,
    columns=['Region', 'Fall_per_100000_inv'],
    key_on='feature.properties.l_id',
    fill_color='YlGn',
    fill_opacity=0.8,
    line_opacity=0.2,
    legend_name='Covid-19'
).add_to(m)

folium.LayerControl().add_to(m)


m.save("map.html")