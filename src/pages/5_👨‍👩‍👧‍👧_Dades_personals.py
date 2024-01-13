from wordcloud import WordCloud
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# Config page
# layout="wide",
st.set_page_config(
                   page_title="Dades personals",
                   page_icon="👨‍👩‍👧‍👧")

# Define font-size
st.markdown("""
<style>
.big-font {
    font-size:19px !important;
}
</style>
""", unsafe_allow_html=True)

# Text
'''
# Dades personals

## Gènere
'''
st.markdown("""<p class="big-font">
Com es d'esperar d'una guerra del segle passat, una gran part dels participants eren homes, i així es veu reflectit al cens de persones
desaparegudes. Visualitzem-ho al següent gràfic de barres.
</p>""", unsafe_allow_html=True)

# Load data
desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")

# Barplot per sex
# figsize=(6,3)
counts = desapareguts.groupby(["Sexe"])["Sexe"].count()
y = [counts["Home"], counts["Dona"]]
x = ["Home", "Dona"]
fig1, ax1 = plt.subplots()
color = ['#1F77B4', '#FFA500']
ax1.bar(x, y, align='center', color=color)
st.pyplot(fig1, use_container_width=True)

# Text
st.markdown("""<p class="big-font">
De manera més concreta, trobem registres de 5177 homes desapareguts, però només 129 corresponents a dones. Representen menys d'un 3% de les
nostres dades!
</p>""", unsafe_allow_html=True)

st.divider()

'''
## Edats
'''
# Text
st.markdown("""<p class="big-font">
Visualitzem mitjançant histogrames la distribució per edats dels desapareguts del cens (tenint en compte només les persones que tenien aquesta 
informació emmagatzemada), separant per gènere per veure si trobem diferències significatives.
</p>""", unsafe_allow_html=True)

# Age comparison
desapareguts_edat = desapareguts.loc[desapareguts["Edat.desaparicio"]!=0]
desapareguts_homes_edat = desapareguts_edat.loc[desapareguts_edat["Sexe"]=="Home"]
desapareguts_dones_edat = desapareguts_edat.loc[desapareguts_edat["Sexe"]=="Dona"]
fig2, ax2 = plt.subplots(1, 2)
ax2[0].hist(desapareguts_homes_edat["Edat.desaparicio"], bins=50)
ax2[0].set_title("Edat homes")
ax2[1].hist(desapareguts_dones_edat["Edat.desaparicio"], bins=50, color="orange")
ax2[1].set_title("Edat dones")
st.pyplot(fig2, use_container_width=True)

# Text
st.markdown("""<p class="big-font">
Cal tenir en compte que el camp "Edat.desaparició" és un camp que es va calcular durant el preprocessament de les dades, a partir de la data de 
desaparició i la data de naixement de cada persona del cens. Per a les persones que no disposaven d'aquesta informació exacta però si de rangs
d'anys de naixement i de desaparició aproximats, es va utilitzar aquesta darrera informació per calcular l'edat que tenien en el moment de la 
desaparició. Per a la resta no es va poder calcular l'edat. Es per això que trobem algunes edats inversemblants als histogrames (menors de 10
anys, per exemple). En qualsevol cas, en general les edats que es mostren als histogrames tenen sentit:
<ul>
  <li class="big-font">
  Els homes presenten un rang d'edats bastant estret, tots eren persones molt joves, principalment entre els 16 i els 35. Es nota que eren
  personal militar en edat de servir.
  </li>
  <li class="big-font">
  Les dones presenten una franja d'edats molt més àmplia i dispersa, on trobem persones joves menors de 20 anys però també tenim pics més enllà
  dels 40. En qualsevol cas, els pics no es poden equiparar als dels homes (veure l'escala de l'eix Y de l'histograma), ja que com hem dit abans,
  aquesta informació s'extreu de les poques dones que trobem al cens.
  </li>
</ul>

Al següent boxplot podem visualitzar de manera més clara els rangs d'edats per gèneres i també revisar si trobem outliers a les dades (valors
que es troben molt distants de la resta d'edats):
</p>""", unsafe_allow_html=True)

# Boxplot
fig3, ax3 = plt.subplots()
my_pal = {"Home": "#1F77B4", "Dona": "#FFA500"}
sns.boxplot(x=desapareguts_edat["Sexe"], y=desapareguts_edat["Edat.desaparicio"], ax=ax3, palette=my_pal)
ax3.set(xlabel='Sexe', ylabel='Edat desaparició')
st.pyplot(fig3, use_container_width=True)

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
st.pyplot(fig4, use_container_width=True)

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
st.pyplot(fig5, use_container_width=True)
