import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Inici"
)

'''
# Desapareguts a la Guerra Civil Espanyola

En aquesta app d'Streamlit, corresponent a la PRA final de l'assignatura de Visualització de Dades 
del Màster en Ciència de Dades de la UOC, explorarem el Cens de persones desaparegudes durant la 
Guerra Civil Espanyola, disponible al [Portal de dades obertes de la Generalitat de Catalunya](https://analisi.transparenciacatalunya.cat/Legislaci-just-cia/Cens-de-persones-desaparegudes-durant-la-Guerra-Ci/u2ix-2jr6/about_data)
eh
'''

desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
st.dataframe(data=desapareguts)
