import pandas as pd


desapareguts = pd.read_csv("data/Cens_de_persones_desaparegudes_durant_la_Guerra_Civil_clean.csv")
provincies = pd.read_csv("data/provincies.csv")

df_naixement = desapareguts.groupby(["Provincia.naixement"])["Provincia.naixement"].count().reset_index(name="count")
df_naixement = df_naixement.merge(provincies, how="left", left_on="Provincia.naixement", right_on="nom_cat")
df_naixement
