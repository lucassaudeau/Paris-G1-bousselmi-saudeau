"""
Created on Mon Feb 27 16:36:56 2023

@author: lucassaudeau
"""

import pandas as pd
import folium

#installer folium :$ conda install -c conda-forge folium

#The variable of the current study, but we can change it with another disaster (e.g. storm, earthquake, volcanic activity...)
study = 'Drought'

#Import database
data = pd.read_csv("/Users/lucassaudeau/Downloads/1900_2021_DISASTERS_DATABASE.csv")

#print(data)
print(data["Disaster Type"].value_counts())

#Processing data to have a clean file without duplicates
data = data.drop_duplicates()

#Our database now only shows data concerning our etude chose (here it is drought)
data = data[data["Disaster Type"] == study] 
#print(data)

#New variable which shows the number of distater type (that we have chosen in study) by countries
event_count = data.groupby(['Country'])['Seq'].count() 

#Estimate the country risk compared to the disaster type
country_risk = event_count / event_count.sum() 

print(event_count)
print("---------------------------")
print(event_count.sum())


#Folium is a python package which allows to visualize world map
m = folium.Map()

#Data concerning the shap of each country to display the map
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
country_shapes = f'{url}/world-countries.json'


folium.Choropleth(
    #The GeoJSON data to represent the world country
    
    #Add country shapes to the map
    geo_data=country_shapes,
    name="choropleth",
    
    #Add data to the map (the country risk about the disaster type studied)
    data=country_risk,
    columns=["Country", "Disaster Type"],
    key_on='feature.properties.name',
    
    #Add the legend on the map
    legend_name=study,
    fill_color='YlOrRd', 
    fill_opacity=0.4, 
    line_opacity=1
).add_to(m)


print(m)

#Save the map to be able to display it, because we can't do it directly on Python/Spyder
m.save('DroughtMap.html')