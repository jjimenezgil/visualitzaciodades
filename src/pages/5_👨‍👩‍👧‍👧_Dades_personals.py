from wordcloud import WordCloud
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# Config page
st.set_page_config(layout="wide",
                   page_title="Dades personals",
                   page_icon="👨‍👩‍👧‍👧")

# Text
'''
# Dades personals

## Gènere
Com es d'esperar d'una guerra del segle passat, una gran part dels participants eren homes, i així es veu reflectit al cens de persones
desaparegudes. Visualitzem-ho al següent gràfic de barres.
'''

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")

# Barplot per sex
counts = desapareguts.groupby(["Sexe"])["Sexe"].count()
y = [counts["Home"], counts["Dona"]]
x = ["Home", "Dona"]
fig1, ax1 = plt.subplots(figsize=(6,3))
color = ['#1F77B4', '#FFA500']
ax1.bar(x, y, align='center', color=color)
st.pyplot(fig1, use_container_width=False)

# Text
'''
De manera més concreta, trobem registres de 5177 homes desapareguts, però només 129 corresponents a dones. Representen menys d'un 3% de les
nostres dades!
'''

st.divider()

'''
## Edats

'''

# Age comparison
desapareguts_edat = desapareguts.loc[desapareguts["Edat.desaparicio"]!=0]
desapareguts_homes_edat = desapareguts_edat.loc[desapareguts_edat["Sexe"]=="Home"]
desapareguts_dones_edat = desapareguts_edat.loc[desapareguts_edat["Sexe"]=="Dona"]
fig2, ax2 = plt.subplots(1, 2, figsize=(6,3))
ax2[0].hist(desapareguts_homes_edat["Edat.desaparicio"], bins=50)
ax2[0].set_title("Edat homes")
ax2[1].hist(desapareguts_dones_edat["Edat.desaparicio"], bins=50, color="orange")
ax2[1].set_title("Edat dones")
st.pyplot(fig2, use_container_width=False)

# Boxplot
fig3, ax3 = plt.subplots(figsize=(6,3))
my_pal = {"Home": "#1F77B4", "Dona": "#FFA500"}
sns.boxplot(x=desapareguts_edat["Sexe"], y=desapareguts_edat["Edat.desaparicio"], ax=ax3, palette=my_pal)
ax3.set(xlabel='Sexe', ylabel='Edat desaparició')
st.pyplot(fig3, use_container_width=False)

# Wordcloud Homes
desapareguts_professio = desapareguts.loc[desapareguts["Professio"].notna()]
desapareguts_homes_professio = desapareguts_professio.loc[desapareguts["Sexe"]=="Home"]

professions_home = desapareguts_homes_professio["Professio"].tolist()
professions_home = list(map(lambda x: x.split(" ")[0].strip(), professions_home))
text_home = ' '.join(professions_home)

wordcloud_home = WordCloud(width = 700,
                      height = 300,
                      collocations=False,
                      max_words=500).generate(text_home)

# Display the generated image:
fig4, ax4 = plt.subplots()
ax4.imshow(wordcloud_home, interpolation='bilinear')
ax4.axis("off")
st.pyplot(fig4, use_container_width=False)

# Wordcloud Dones
desapareguts_dones_professio = desapareguts_professio.loc[desapareguts["Sexe"]=="Dona"]
professions_dona = desapareguts_dones_professio["Professio"].tolist()
professions_dona = list(map(lambda x: x.split(" ")[0].strip(), professions_dona))
text_dona = ' '.join(professions_dona)

wordcloud_dona = WordCloud(width = 700, 
                           height = 300,
                           collocations=False,
                           max_words=500).generate(text_dona)

# Display the generated image:
fig5, ax5 = plt.subplots()
ax5.imshow(wordcloud_dona, interpolation='bilinear')
ax5.axis("off")
st.pyplot(fig5, use_container_width=False)
