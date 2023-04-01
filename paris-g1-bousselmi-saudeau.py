#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:36:56 2023

@author: lucassaudeau
"""
import pandas as pd
import folium

#installer folium : $ conda install -c conda-forge folium

etude = 'Wildfire'


data = pd.read_csv('1900_2021_DISASTERS.xlsx - emdat data.csv')
#print(data)
print(data['Disaster Type'].value_counts())

data = data.drop_duplicates()
data = data[data['Disaster Type'] == etude] 
#print(data)


event_count = data.groupby(['Country'])['Seq'].count() 
country_risk = event_count / event_count.sum() 

#print(event_count)
#print("---------------------------")
#print(event_count.sum())

m = folium.Map()

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
country_shapes = f'{url}/world-countries.json'

folium.Choropleth(
    #The GeoJSON data to represent the world country
    
    geo_data=country_shapes,
    name="choropleth",
    
    
    data=country_risk,
    columns=["Country", "Disaster Type"],
    key_on='feature.properties.name',
    

    legend_name=etude,
    fill_color='YlOrRd', 
    fill_opacity=0.4, 
    line_opacity=1
).add_to(m)


print(m)

m.save('maCarte.html')
