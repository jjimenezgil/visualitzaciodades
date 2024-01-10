# import folium
import pandas as pd
import streamlit as st
# from streamlit_folium import folium_static


# Config page
st.set_page_config(layout="wide")

# Load data
desapareguts = pd.read_csv("../data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
provincies = pd.read_csv("../data/provincies.csv")

# Join data with provinces information
df_naixement = desapareguts.groupby(["Provincia.naixement"])["Provincia.naixement"].count().reset_index(name="count")
df_naixement = df_naixement.merge(provincies, how="left", left_on="Provincia.naixement", right_on="nom_cat")
st.dataframe(data=df_naixement, hide_index=True)

# Create select box for the different maps
choice = ['Mapa de les províncies de naixement de les persones desaparegudes',
          'Mapa de les províncies habituals de les persones desaparegudes', 
          'Mapa de les províncies on es van produir les desaparicions', 
          'Mapa de les províncies on es van produir els afusellaments',
          'Mapa de les províncies on es van localitzar els cosos de les persones desaparegudes']
choice_selected = st.selectbox("Selecciona el mapa", choice, index=2)

# Create map
# m = folium.Map(location=[40.41, -3.7], tiles='CartoDB positron', zoom_start=5)
