from wordcloud import WordCloud
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# Config page
st.set_page_config(page_title="Dades personals",
                   page_icon="👨‍👩‍👧‍👧")

# Text
'''
# Dades personals
'''

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")

# Histogram per sex
counts = desapareguts.groupby(["Sexe"])["Sexe"].count()
y = [counts["Home"], counts["Dona"]]
x = ["Home", "Dona"]
fig1, ax1 = plt.subplots()
ax1.bar(x, y, align='center')
st.pyplot(fig1)

# Age comparison
desapareguts_edat = desapareguts.loc[desapareguts["Edat.desaparicio"]!=0]
desapareguts_homes_edat = desapareguts_edat.loc[desapareguts_edat["Sexe"]=="Home"]
desapareguts_dones_edat = desapareguts_edat.loc[desapareguts_edat["Sexe"]=="Dona"]
fig2, ax2 = plt.subplots(1, 2, figsize=(12,5))
ax2[0].hist(desapareguts_homes_edat["Edat.desaparicio"], bins=50)
ax2[0].set_title("Edat homes")
ax2[1].hist(desapareguts_dones_edat["Edat.desaparicio"], bins=50, color="orange")
ax2[1].set_title("Edat dones")
st.pyplot(fig2)

# Boxplot
fig3, ax3 = plt.subplots()
sns.boxplot(x=desapareguts_edat["Sexe"], y=desapareguts_edat["Edat.desaparicio"], ax=ax3)
st.pyplot(fig3)

# Wordcloud
desapareguts_homes = desapareguts.loc[desapareguts["Sexe"]=="Home"]
desapareguts_homes_professio = desapareguts_homes.loc[desapareguts["Professio"].notna()]
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
