import streamlit as st
import pandas as pd
import numpy as np
import a56 as a56 # posso importar variáveis de outros arquivos python
import altair as alt
import plotly.graph_objects as go



#iniciando comandos de streamlit

st.markdown("# Cruzando dados de escolas")
st.markdown("## Reading Score per School")

# uma vez prontos, basta escrever no terminal "Streamlit + run + nome do arquivo"
#notar que para poder rodar corretamente o nome do arquivo é preciso que o cwd (central work directory)
# esteja na pasta correta onde está o arquivo .py (com o comando streamlit)
#que você irá rodar.
# para chegar lá, é possivel "aprofundar" nos diretórios através do comando "cd" + espaço + tab
# que irá mostrar as pastas que há dentro da macro pasta que voce está. quando chegar na pasta onde
# o arquivo .py está salvo, somente digite o comando para executar o streamlit, e ele irá criar um
# site com os dados que voce inseriu no código

# importante: no site com o código há uma opção de "rerun", que irá rodar o código dentro do python
# com as atualizações, ao invés de ter que enviar o comando de novo de streamlit run codigo.py

#note que é PRECISO SALVAR o arquivo antes de dar rerun, porque ele irá buscar justamente
#os arquivos salvos

#ACESSO A DOCUMENTACAO DO STREAMLIT ACESSAR SITE--> DOCUMENTATION --> API REFERENCE

st.dataframe(a56.school_data_reading)

st.line_chart(a56.school_data_reading, x= "reading_score", y= "budget")

chart = alt.Chart(a56.school_data_math).mark_circle().encode(
    x="math_score",
    y="budget",
    color ="school_name"
) # criou-se um gráfico usando outra biblioteca, a altair

# agora irei pegar o suporte do streamlit para essa biblioteca, o st.altair_chart

st.altair_chart(chart,use_container_width=True)


