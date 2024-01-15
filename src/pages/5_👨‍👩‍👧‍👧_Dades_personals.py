from wordcloud import WordCloud
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots


# Config page
st.set_page_config(
                   page_title="Dades personals",
                   page_icon="👨‍👩‍👧‍👧")

# Define font-size
st.markdown("""
<style>
.big-font {
    font-size:18px !important;
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
countPerSexe = desapareguts.groupby(["Sexe"])["Id"].count().reset_index(name="Desapareguts")
fig1 = px.bar(countPerSexe, x="Sexe", y="Desapareguts", color="Sexe")
st.plotly_chart(fig1, use_container_width=True)

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
fig2 = make_subplots(rows=1, cols=2, subplot_titles=('Edat dones', 'Edat homes'))

hist1 = px.histogram(desapareguts_dones_edat, x="Edat.desaparicio", 
                     opacity=0.8, color_discrete_sequence=['#83C9FF'], nbins=70)
hist2 = px.histogram(desapareguts_homes_edat, x="Edat.desaparicio", 
                     opacity=0.8, color_discrete_sequence=['#0068C9'], nbins=70)

figure1_traces = []
figure2_traces = []
for trace in range(len(hist1["data"])):
    figure1_traces.append(hist1["data"][trace])
for trace in range(len(hist2["data"])):
    figure2_traces.append(hist2["data"][trace])

# Get the Express fig broken down as traces and add the traces to the proper plot within in the subplot
for traces in figure1_traces:
    fig2.append_trace(traces, row=1, col=1)
for traces in figure2_traces:
    fig2.append_trace(traces, row=1, col=2)
st.plotly_chart(fig2, use_container_width=True)


# Text
st.markdown("""<p class="big-font">
Cal tenir en compte que el camp "Edat.desaparició" és un camp que es va calcular durant el preprocessament de les dades, a partir de la data de 
desaparició i la data de naixement de cada persona del cens. Per a les persones que no disposaven d'aquesta informació exacta però sí de rangs
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
</p>""", unsafe_allow_html=True)

st.markdown("""<p class="big-font">
Al següent boxplot podem visualitzar de manera més clara els rangs d'edats per gèneres i també revisar si trobem outliers a les dades (valors
que es troben molt distants de la resta d'edats):
</p>""", unsafe_allow_html=True)

# Boxplot
desapareguts_edat.sort_values(by="Sexe", ascending=True, inplace=True)
fig3 = px.box(desapareguts_edat, y="Edat.desaparicio", color="Sexe")
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Text
'''
## Ocupacions

### Homes
'''
st.markdown("""<p class="big-font">
Al següent "wordcloud" o núvol de paraules s'exposen les ocupacions dels homes desapareguts durant la Guerra Civil, de tal manera que les 
ocupacions més freqüents són les que es presenten en primer plà i en mides més grans, i al contrari per a la resta de professions menys freqüents:
</p>""", unsafe_allow_html=True)

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

# Text
st.markdown("""<p class="big-font">
Aquestes ocupacions son un reflex de la societat espanyola del moment: una gran majoria dels homes es dedicaven als sectors primari i secundari
(pagesos, jornalers, forners, fusters, paletes, obrers...). Això també ens diu que una gran majoria de les persones que van participar en la
Guerra Civil no era personal militar, si no treballadors normals que es van veure abocats a aquesta catàstrofe. Tot i així, també apareixen de
manera bastant destacada algunes ocupacions militars i policials (militar, guárdia, carrabiner...). Sorprèn també l'aparició en primer plà de
la professio de capellà, seria interessant saber si van participar com a combatents o donant servei sacerdotal als militar d'un i altre bàndol.
Per últim, destacar també l'elevat nombre d'estudiants que hi van participar, qui sap si de manera obligatòria o per idealisme (veure l'apartat
amb les [dades bèl·liques](https://visualitzaciodadespra-personesdesaparegudesguerracivil.streamlit.app/Dades_b%C3%A8l%C2%B7liques) per saber
la quantitat de voluntaris que trobem al nostre cens.
</p>""", unsafe_allow_html=True)

'''
### Dones
'''

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

# Text
st.markdown("""<p class="big-font">
Tot i que tenim molt poca informació, trobem professions molt més especialitzades (mestres i infermeres), tot i que de fons també trobem el 
mateix popurri de professions que teníem al gènere masculí: pagesses, forneres, minyones, assistents, monjes, botigueres, etc. És d'esperar
que les infermeres participessin a la guerra en qualitat de serveis mèdics i no pas com a combatents. Pel que fa a les mestres i la resta de
dones amb altres ocupacions, no és fàcil saber quin va ser el seu paper a la guerra. No es pot descartar que algunes hi participessin com a 
combatents, ja que la Guerra Civil Espanyola és un dels primers conflictes on les dones van participar en gran número al combat i en funcions
de recolzament al front (a diferència, per exemple, de la Primera Guerra Mundial).
</p>""", unsafe_allow_html=True)
