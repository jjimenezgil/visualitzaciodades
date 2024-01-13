import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Inici"
)

'''
# Desapareguts a la Guerra Civil Espanyola

En aquesta app d'Streamlit, corresponent a la PRA final de l'assignatura de Visualització de Dades del Màster en Ciència de Dades de la UOC de
l'alumne Javier Jiménez Gil, explorarem el Cens de persones desaparegudes durant la Guerra Civil Espanyola, disponible al 
[Portal de dades obertes de la Generalitat de Catalunya](https://analisi.transparenciacatalunya.cat/Legislaci-just-cia/Cens-de-persones-desaparegudes-durant-la-Guerra-Ci/u2ix-2jr6/about_data).
Intentarem respondre una sèrie de preguntes plantejades prèviament, que es detallaven a la primera entrega de la PRA, i que bàsicament es centraven
en diferents àmbits de les vides de les persones desaparegudes:

* Àmbit geogràfic: En quines províncies van neixer les persones desaparegudes? En quines províncies van desapareixer? En cas de no haver
desaparegut a Espanya, a quin país ho van fer?
* Àmbit cronològic: En quins anys es van produir més desaparicions? Trobem un nombre significatiu de desapareguts també posteriorment al 1939, 
és a dir, durant la Dictadura?
* Àmbit bèl·lic: Trobem que la majoria de desapareguts eren militars o civils? Eren voluntaris o els van llevar de manera obligatòria? 
En quin exercit van lluitar? Quants van ser afusellats?
* Àmbit personal: A què es dedicaven les persones desaparegudes? Quines edats tenien? Ha sigut possible localitzar un nombre significatiu 
de persones desaparegudes? On han estat localitzades? Tot i tenir menys d’un 3% de les dades dedicades a les dones, s'intenta aplicar la 
perspectiva de gènere per tal de poder entreveure també qui eren i a que es dedicaven les dones que van desapareixer durant la Guerra Civil.

A la taula següent podeu observar les dades un cop netejades i processades. Us animo a accedir a les quatre pestanyes que trobareu a la barra 
lateral esquerra per explorar els diferents aspectes d'aquest projecte de visualització de dades i intentar trobar respostes a les preguntes
plantejades!
'''

desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
st.dataframe(data=desapareguts, hide_index=True)

'''
Al meu [repositori de Github](https://github.com/jjimenezgil/visualitzaciodadesPRA) podeu trobar el codi del projecte amb llicència de
codi obert. Adreçeu-vos al fitxer README.txt per conèixer els detalls i l'estructura del projecte.
'''
