import folium
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static


# Config page
st.set_page_config(layout="wide")

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
provincies = pd.read_csv("data/provincies.csv")

# Join data with provinces information
df_naixement = desapareguts.groupby(["Provincia.naixement"])["Provincia.naixement"].count().reset_index(name="count")
df_naixement = df_naixement.merge(provincies, how="left", left_on="Provincia.naixement", right_on="nom_cat")

# Create map
m = folium.Map(location=[40.41, -3.7], tiles='CartoDB positron', zoom_start=5)
