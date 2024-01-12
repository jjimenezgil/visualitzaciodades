from wordcloud import WordCloud
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# Config page
st.set_page_config(page_title="Dades personals",
                   page_icon="👨‍👩‍👧‍👧")

# Text
'''
# Dades personals
'''

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
desapareguts_homes = desapareguts.loc[desapareguts["Sexe"]=="Home"]
desapareguts_homes_professio = desapareguts_homes.loc[desapareguts["Professio"].notna()]

# Histogram per sex
counts = desapareguts.groupby(["Sexe"])["Sexe"].count()
y = [counts["Home"], counts["Dona"]]
x = ["Home", "Dona"]
fig1, ax1 = plt.subplots()
ax1.bar(x, y, align='center')
st.pyplot(fig1)



professions = desapareguts_homes_professio["Professio"].tolist()
professions = list(map(lambda x: x.split(" ")[0].strip(), professions))
text = ' '.join(professions)


wordcloud = WordCloud(width = 700,
                      height = 300,
                      collocations=False,
                      max_words=500).generate(text)

# Display the generated image:
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)
