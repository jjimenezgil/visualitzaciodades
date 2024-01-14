import pandas as pd
import plotly.express as px
import streamlit as st


# Config page
st.set_page_config(layout="wide",
                   page_title="Dades cronològiques",
                   page_icon="⏱️")

# Text
'''
# Dades cronològiques
'''
st.markdown("""<p class="big-font">
En aquesta secció visualitzarem el nombre de desaparicions en funció del temps, per veure quins van ser els pitjors anys i també si es van 
seguir produint desaparicions un cop finalitzada la Guerra Civil, és a dir, durant la dictadura. Podeu manipular el següent gràfic (fer zoom,
moure els eixos, mostrar les dades només d'homes o dones o ambdues a la vegada...).
</p>""", unsafe_allow_html=True)

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
desapareguts_aux = desapareguts[desapareguts["Any.desaparicio"]>0]
anys_desaparicio = desapareguts_aux.groupby(["Any.desaparicio", "Sexe"])["Any.desaparicio"].count().reset_index(name="Desapareguts")
anys_desaparicio.rename(columns={"Any.desaparicio": "Any"}, inplace=True)

# Draw temporal lines with Plotly
fig = px.line(anys_desaparicio, x="Any", y="Desapareguts", color="Sexe")
fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 1935,
        dtick = 1,
        tickangle = 45
    )
)
fig.add_shape(
    name="Final Guerra Civil",
    showlegend=True,
    type="line",
    line=dict(dash="dash"),
    x0=1939,
    x1=1939,
    y0=0,
    y1=2500,
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""<p class="big-font">
Trobem que el pitjor any, tant per al gènere masculí com femení, és el 1938, amb 2533 i 38 desaparicions respectivament. A partir d'aquí el nombre
de desaparicions va disminuint, tot i que se'n continuen produint durant la Dictadura però en quantitats molt menors. Per a les dones la darrera 
desaparició es va produir a l'any 1948, però per als homes en trobem 1 o 2 a l'any fins a arribar al 1973, és a dir, fins gairebé el final de la 
Dictadura, que es va produir en 1975.
</p>""", unsafe_allow_html=True)
