import pandas as pd
import plotly.express as px
import streamlit as st


# Config page
st.set_page_config(layout="wide",
                   page_title="Dades bèl·liques",
                   page_icon="💣")

# Text
'''
# Dades bèl·liques
'''
st.markdown("""<p class="big-font">
En aquesta secció visualitzarem ...
</p>""", unsafe_allow_html=True)

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
desapareguts.loc[desapareguts["Es.voluntari"]==1, "Es.voluntari"] = "Voluntari"
desapareguts.loc[desapareguts["Es.voluntari"]==0, "Es.voluntari"] = "No voluntari"
desapareguts.loc[desapareguts["Es.afusellat"]==1, "Es.afusellat"] = "Afussellat"
desapareguts.loc[desapareguts["Es.afusellat"]==0, "Es.afusellat"] = "No afussellat"

# Prepare data
desapareguts_grouped_vol = desapareguts.groupby(["Es.voluntari", "Exercit"])["Id"].count().reset_index(name="Desapareguts")
desapareguts_grouped_af = desapareguts.groupby(["Es.afusellat", "Exercit"])["Id"].count().reset_index(name="Desapareguts")

# Stacked barplot
fig1 = px.bar(desapareguts_grouped_vol, x="Es.voluntari", y="Desapareguts", color="Exercit")

# Show plot
fig1.update_layout(xaxis = dict(
                              title = 'Eren voluntaris?', 
                              title_font_size = 16) 
                 ) 
st.plotly_chart(fig1, use_container_width=True)

# Stacked barplot
fig2 = px.bar(desapareguts_grouped_af, x="Es.afusellat", y="Desapareguts", color="Exercit")

# Show plot
fig2.update_layout(xaxis = dict(
                              title = 'Van ser afussellats?', 
                              title_font_size = 16) 
                 ) 
st.plotly_chart(fig2, use_container_width=True)
