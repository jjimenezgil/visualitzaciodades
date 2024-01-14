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

# Prepare data
desapareguts_grouped = desapareguts.groupby(["Es.voluntari", "Exercit"])["Id"].count().reset_index(name="Desapareguts")

# Stacked barplot
fig = px.bar(desapareguts_grouped, x="Es.voluntari", y="Desapareguts", color="Exercit")

# Show plot
fig.update_layout(title = 'Composició dels exèrcits', 
                 title_font_size = 22,
                 title_x=0.5,
                 xaxis = dict(
                              title = 'Eren voluntaris?', 
                              title_font_size = 14) 
                 ) 
st.plotly_chart(fig, use_container_width=True)
