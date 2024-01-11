import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import json
import geopandas


# Config page
st.set_page_config(layout="wide",
                   page_title="Dades geogràfiques",
                   page_icon="🌍")

# Text
'''
# Dades geogràfiques

### Persones desaparegudes a Espanya

Al Cens de persones desaparegudes durant la Guerra Civil hi figura molta informació geogràfica: on
van neixer les persones desaparegudes, on era la seva residència habitual, on van desapareixer, on
van ser localitzats... Explorem tota aquesta informació, organitzada per províncies, al següent mapa.
'''

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
provincies = pd.read_csv("data/provincies.csv")
paisos = pd.read_csv("data/countries.csv")
with open("data/spain-provinces.geojson") as f:
    geojson_data = json.load(f)
geodf = geopandas.GeoDataFrame.from_features(geojson_data, crs="EPSG:4326")
with open('data/countries.geojson') as f:
    c = json.load(f)
geodf_countries = geopandas.GeoDataFrame.from_features(c, crs="EPSG:4326")

# Counts per province
df_naixement = desapareguts.groupby(["Provincia.naixement"])["Provincia.naixement"].count().reset_index(name="countNaixement")
df_habitual = desapareguts.groupby(["Provincia.habitual"])["Provincia.habitual"].count().reset_index(name="countHabitual")
df_desaparicio = desapareguts.groupby(["Provincia.desaparicio"])["Provincia.desaparicio"].count().reset_index(name="countDesaparicio")
df_afusellament = desapareguts.groupby(["Provincia.afusellament"])["Provincia.afusellament"].count().reset_index(name="countAfusellament")
df_localització = desapareguts.groupby(["Provincia.localitzat"])["Provincia.localitzat"].count().reset_index(name="countLocalitzacio")

# Join to get full information in a single geodf
df_final = provincies.merge(df_naixement, how="outer", left_on="nom_cat", right_on="Provincia.naixement")
df_final = df_final.merge(df_habitual, how="outer", left_on="nom_cat", right_on="Provincia.habitual")
df_final = df_final.merge(df_desaparicio, how="outer", left_on="nom_cat", right_on="Provincia.desaparicio")
df_final = df_final.merge(df_afusellament, how="outer", left_on="nom_cat", right_on="Provincia.afusellament")
df_final = df_final.merge(df_localització, how="outer", left_on="nom_cat", right_on="Provincia.localitzat")
df_final.drop(labels=["Provincia.naixement","Provincia.habitual","Provincia.desaparicio","Provincia.afusellament","Provincia.localitzat"], axis=1, inplace=True)
geo_df_final = geodf.merge(df_final, how="outer", left_on="name", right_on="nom_GeoJSON")

# Create select box for the different maps
choice = ['Mapa de les províncies de naixement de les persones desaparegudes',
          'Mapa de les províncies habituals de les persones desaparegudes', 
          'Mapa de les províncies on es van produir les desaparicions', 
          'Mapa de les províncies on es van produir els afusellaments',
          'Mapa de les províncies on es van localitzar els cossos de les persones desaparegudes']
choice_selected = st.selectbox("Selecciona el mapa", choice, index=2)

countToShow = "countDesaparicio"
if choice_selected == choice[0]:
  countToShow = "countNaixement"
elif choice_selected == choice[1]:
  countToShow = "countHabitual"
elif choice_selected == choice[2]:
  countToShow = "countDesaparicio"
elif choice_selected == choice[3]:
  countToShow = "countAfusellament"
else:
  countToShow = "countLocalitzacio"
  
# Create map
m = folium.Map(location=[40.41, -3.7], tiles='CartoDB positron', zoom_start=6)

# Append Choropleth colors to map
folium.Choropleth(
    geo_data=geo_df_final,
    name="choropleth",
    data=geo_df_final,
    columns= ["cod_prov", countToShow],
    key_on="feature.properties.cod_prov",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.1,
    legend_name=choice_selected).add_to(m)

# Append geoJSON province limits to the map
tooltip = folium.GeoJsonTooltip(
    fields=["nom_cat", countToShow],
    aliases=["Província:", "Nombre de desapareguts:"],
    localize=True,
    sticky=False,
    labels=True
)
folium.GeoJson(geo_df_final, name="Provinces map", tooltip=tooltip).add_to(m)

# Show map
folium_static(m, width=1000, height=600)

# Text
'''
En tractar-se d'un registre de dades de la Generalitat de Catalunya, no sorpren descubrir als mapes que la majoria de persones desaparegudes
eren nascudes o habitants de Catalunya, o bé van desapareixer a Catalunya (o totes les anteriors a la vegada). El fet que Barcelona fos una de
les últimes ciutats del bandol republicà en caure sota el control dels nacionals també pot estar relacionat amb l'elevat nombre de persones
desaparegudes a l'esmentada ciutat. També a Catalunya (i especialment Barcelona) és on hi ha un major nombre de cossos localitzats i recuperats.
Tot i que la major part de l'informació que trobem als mapes era d'esperar, en podem destacar un parell de fets:

* Barcelona és la ciutat més destacada als diferents mapes (és el lloc on van neixer i viure més persones del registre de desapareguts, i 
també on més persones van ser afusellades i on més persones han sigut localitzades), però sorpren el fet que, si observem
el mapa de les províncies on es van produir les desaparicions, Barcelona es veu àmpliament superada per Tarragona i LLeida.
* A Terol també trobem un nom sorprenentment alt de desapareguts (235), només superat per algunes de les províncies catalanes.

### Persones desaparegudes a l'estranger

Al següent mapa es mostren el nombre de persones registrades al Cens de persones desaparegudes durant la Guerra Civil que van desapareixer
a països estrangers.
'''

# Count and joins per country
df_paisos = desapareguts.groupby(["Pais.desaparicio"])["Pais.desaparicio"].count().reset_index(name="count")
df_paisos = df_paisos.merge(paisos, how="outer", left_on="Pais.desaparicio", right_on="nom_cat")
geo_df_paisos = geodf_countries.merge(df_paisos, how="inner", left_on="name_es", right_on="name_es")
# Remove Spain
geo_df_paisos = geo_df_paisos.loc[geo_df_paisos["name_es"] != "España"]

# Country map
m2 = folium.Map(location=[50.37, 15], tiles='CartoDB positron', zoom_start=2)
folium.Choropleth(
    geo_data=geo_df_paisos,
    name="choropleth",
    data=geo_df_paisos,
    columns= ["name_es", "count"],
    key_on="feature.properties.name_es",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.1,
    legend_name="Nombre de desapareguts a l'estranger").add_to(m2)
tooltip2 = folium.GeoJsonTooltip(
    fields=["nom_cat", "count"],
    aliases=["País:", "Nombre de desapareguts:"],
    localize=True,
    sticky=False,
    labels=True
)
folium.GeoJson(geo_df_paisos, name="Countries map", tooltip=tooltip2).add_to(m2)
folium_static(m2, width=1000, height=600)

'''
En aquest cas, és coherent que la major part de desaparicions a l'estranger s'enregistressin a França, el país on es va exiliar
una gran part de la població espanyola. Les desaparicions a altres països com ara Rússia o Alemanya són pràcticament testimonials,
al menys amb la informació de que disposem en aquest cens.
'''
