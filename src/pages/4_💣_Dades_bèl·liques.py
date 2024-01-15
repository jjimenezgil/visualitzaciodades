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

## Tropes voluntàries
'''
st.markdown("""<p class="big-font">
En aquesta secció visualitzarem el nombre de tropes voluntàries i no voluntàries en funció de a quin exèrcit pertanyien: republicans o 
rebels (també conegut com bàndol nacional).
</p>""", unsafe_allow_html=True)

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
desapareguts.loc[desapareguts["Es.voluntari"]==1, "Es.voluntari"] = "Voluntari"
desapareguts.loc[desapareguts["Es.voluntari"]==0, "Es.voluntari"] = "No voluntari"
desapareguts.loc[desapareguts["Es.afusellat"]==1, "Es.afusellat"] = "Afussellat"
desapareguts.loc[desapareguts["Es.afusellat"]==0, "Es.afusellat"] = "No afussellat"

# Prepare data
desapareguts_grouped_vol = desapareguts.groupby(["Exercit","Es.voluntari"])["Id"].count().reset_index(name="Desapareguts")
desapareguts_grouped_af = desapareguts.groupby(["Exercit","Es.afusellat"])["Id"].count().reset_index(name="Desapareguts")

# Stacked barplot
fig1 = px.bar(desapareguts_grouped_vol, x="Exercit", y="Desapareguts", color="Es.voluntari")

# Show plot
fig1.update_layout(xaxis = dict(
                              title = 'Eren voluntaris?', 
                              title_font_size = 16) 
                 ) 
st.plotly_chart(fig1, use_container_width=True)

# Text
st.markdown("""<p class="big-font">
Trobem que el cens de persones desaparegudes està conformat en gran part per desapareguts de l'exèrcit republicà, i només hi consten 139 persones
del bàndol rebel. També hi ha un elevat nombre de persones (1772) per a les quals no es coneix el bàndol en el qual van lluitar. Pel que fa als 
voluntaris, en trobem molt pocs independentment de l'exèrcit (republicà, nacional o desconegut). Podem concloure, doncs, que la major part
de les persones registrades al cens de persones desaparegudes de la Generalitat de Catalunya van ser llevades de manera obligatòria. Es recomanable
fer zoom a les diferents parts del gràfic de barres per conèixer de manera exacta el nombre de voluntaris i no voluntaris de cada exèrcit.
</p>""", unsafe_allow_html=True)

st.divider()

# Text
'''
## Afussellaments
'''
st.markdown("""<p class="big-font">
En aquesta secció
</p>""", unsafe_allow_html=True)

# Stacked barplot
fig2 = px.bar(desapareguts_grouped_af, x="Exercit", y="Desapareguts", color="Es.afusellat")

# Show plot
fig2.update_layout(xaxis = dict(
                              title = 'Van ser afussellats?', 
                              title_font_size = 16) 
                 ) 
st.plotly_chart(fig2, use_container_width=True)
