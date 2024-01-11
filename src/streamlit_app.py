import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Desapareguts a la guerra civil Espanyola",
    page_icon="📈",
)

st.markdown("# Desapareguts a la Guerra Civil Espanyola")

desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")

st.dataframe(data=desapareguts)
