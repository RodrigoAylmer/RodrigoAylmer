import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.graph_objects as go

data1 = pd.read_excel("C:/Users/rdy/OneDrive - Danske Commodities/Desktop/Motim/Bibliotecas/teste sankey.xlsx",sheet_name="source-target")
data2 = pd.read_excel("C:/Users/rdy/OneDrive - Danske Commodities/Desktop/Motim/Bibliotecas/teste sankey.xlsx",sheet_name="target-source")


sectors = sorted(["Açúcar", "Petróleo", "Ovos", "Indústria", "Aço", "Bancário"])

colors = ["blue", "green", "red", "yellow", "purple", "orange"] # uma cor para cada setor

source_labels = [f"{sector}" for sector in sectors]
target_labels = [f"{sector}_target" for sector in sectors]
destination_labels = [f"{sector}_final" for sector in sectors]

labels = source_labels + target_labels + destination_labels
# Crie listas para armazenar os valores de origem, destino e valor
sources = []
targets = []
values = []

# Preencha as listas com os dados da matriz 1
for i in range(1,len(data1)):
    for j in range(2,len(data1.columns)):
            sources.append(i-1)
            targets.append(j-2 + len(sectors)) #isso aqui é para que o index dos labels bata corretamente.
            values.append(data1.iloc[i, j])

# Preencha as listas com os dados da matriz 2
for i in range(1,len(data2)):
    for j in range(2,len(data2.columns)):
            sources.append(i-1 + len(sectors))
            targets.append(j-2 + 2*len(sectors)) #isso aqui é para que o index dos labels bata corretamente.
            values.append(data2.iloc[i, j])




# Crie o gráfico de Sankey
fig = go.Figure(data=go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label= labels,
        color=colors*3
    ),
    link=dict(
        source=sources,  # índices correspondem aos rótulos
        target=targets,
        value=values
    )
))

fig.update_layout(title_text="Gráfico de Sankey a partir de uma matriz", font_size=10)

# Exiba o gráfico no Streamlit
st.plotly_chart(fig)


