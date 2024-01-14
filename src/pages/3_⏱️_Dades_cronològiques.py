import pandas as pd
import plotly.express as px


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
fig.show()
