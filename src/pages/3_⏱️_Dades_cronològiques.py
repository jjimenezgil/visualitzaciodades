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
En aquesta 
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
