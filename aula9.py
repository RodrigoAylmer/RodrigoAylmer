# vamos usar a biblioteca do Yfinance - Yahoo Finance
#para isso precisamos primeiro baixar com pip install

import yfinance as yf # conteúdo da aula 9 a 12
import pandas as pd
import streamlit as st
from datetime import datetime

st.markdown("# Analisando empresas") # ao colocar o "#" se faz um título no nível 1 (maior)

st.text_input("Ticker code", key="tickercode", value="GOOG") # o value estabelece um valor padrão pro ticker code

ticker = st.session_state.tickercode

st.markdown(f"## Últimas Notícias da {st.session_state.tickercode}: ") # ao se colocar "##" se faz um título nível 2. máximo que vai é nível 6




data = yf.Ticker(ticker)



r = data.news # vai retornar as notícias recentes da empresa colocada
# print(r)
# print("\n"*20)

# print(r[0].keys())

titulos = []
noticias = []
for key in r:
    # print(key["title"])
    # print(key["link"])
    # print("\n"*2)
    titulos.append(key["title"])
    noticias.append(key["link"])


# print(titulos)
# print(noticias)


#o tipo de dados que estamos mexendo é "pandas.core.frame.DataFrame", ou seja, estamos trabalhando com pandas

# '''
# Tabela de periodos possíveis no .history():

# Código          significado     máximo de dias

# 1m              1 minute        7 dias
# 2m              2 minutes       60 dias
# 5m              5 minutes       60 dias
# 15m             15 minutes      60 dias
# 30m             30 minutes      60 dias
# 60m             60 minutes      730 dias
# 90m             90 minutes      60 dias
# 1h              1 hour          730 dias
# 1d              1 day           total do histórico
# 5d              5 days          total do histórico
# 1wk             1 week          total do histórico
# 1mo             1 month         total do histórico
# 3mo             3 months        total do histórico

# ao colocar máximo, eu coleto o máximo que eu puder de granularidade dentro do start e end que estabeleci.


# '''


acionistas = data.major_holders
# print(acionistas)


# ''' -------------------------------------------------- aula 10 e 11-------------------------------------------------------'''

data_news = data.news
data_news = pd.DataFrame(data.news)
data_news2 = data_news[["title", "publisher", "link","relatedTickers"]]
st.dataframe(data_news2)
end_date = datetime.now().strftime("%Y-%m-%d")

data_hist = data.history(period="max",start="2019-3-16", end=end_date,interval="5d") #.history() --> coleta dados históricos das ações pro que voce definiu
#periodo --> periodos 

data_hist = data_hist.reset_index() # necessário fazer pois a coluna de datas está tratando "date" como um índex e não como um nome de coluna

ey = st.selectbox("Eixo y:", data_hist.columns)
ex = st.selectbox("Eixo x:", data_hist.columns)



st.markdown(f"## Gráfico de {ey} x {ex}:")
st.line_chart(data_hist, x= ex, y=ey)

#------------------------------------------------- aula 12 ----------------------------------------------------------------------





