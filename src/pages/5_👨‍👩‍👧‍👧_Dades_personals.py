from wordcloud import WordCloud
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
desapareguts_homes = desapareguts.loc[desapareguts["Sexe"]=="Home"]
desapareguts_homes_professio = desapareguts_homes.loc[desapareguts["Professio"].notna()]

professions = desapareguts_homes_professio["Professio"].tolist()
professions = list(map(lambda x: x.split(" ")[0].strip(), professions))
text = ' '.join(professions)

# background_color="white"
wordcloud = WordCloud(width = 700,
                      height = 300,
                      collocations=False,
                      max_words=500).generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
