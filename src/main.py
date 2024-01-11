import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import json
import geopandas


# Config page
st.set_page_config(layout="wide")

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
provincies = pd.read_csv("data/provincies.csv")
with open("data/spain-provinces.geojson") as f:
    geojson_data = json.load(f)
geodf = geopandas.GeoDataFrame.from_features(geojson_data, crs="EPSG:4326")

# Join data with provinces information
df_naixement = desapareguts.groupby(["Provincia.naixement"])["Provincia.naixement"].count().reset_index(name="count")
df_naixement = df_naixement.merge(provincies, how="left", left_on="Provincia.naixement", right_on="nom_cat")
df_naixement = geodf.merge(df_naixement, how="left", left_on="name", right_on="nom_GeoJSON")

# Create select box for the different maps
choice = ['Mapa de les províncies de naixement de les persones desaparegudes',
          'Mapa de les províncies habituals de les persones desaparegudes', 
          'Mapa de les províncies on es van produir les desaparicions', 
          'Mapa de les províncies on es van produir els afusellaments',
          'Mapa de les províncies on es van localitzar els cosos de les persones desaparegudes']
choice_selected = st.selectbox("Selecciona el mapa", choice, index=2)

# Create map
m = folium.Map(location=[40.41, -3.7], tiles='CartoDB positron', zoom_start=6)

# Append geoJSON province limits to the map
tooltip = folium.GeoJsonTooltip(
    fields=["nom_cat", "count"],
    aliases=["Província:", "Nombre de desapareguts:"],
    localize=True,
    sticky=False,
    labels=True
)
folium.GeoJson(df_naixement, name="Provinces map", tooltip=tooltip).add_to(m)

# Append Choropleth colors to map
"""folium.Choropleth(
    geo_data=df_naixement,
    name="choropleth",
    data=df_naixement,
    columns= ["GEOID","Total_Pop_2021"],
    key_on="feature.properties.GEOID",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=choice).add_to(m)"""

folium.LayerControl().add_to(m)

# Show map
folium_static(m, width=1200, height=650)
st.dataframe(data=pd.DataFrame(df_naixement))
