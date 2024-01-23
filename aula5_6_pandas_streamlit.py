import pandas as pd #importante gerar um apelido que simplifique a escrita do código
import numpy as np 

def ler_csv(nome):
    nome = "C:/Users/rdy/OneDrive - Danske Commodities/Danske/Python/Motim/Bibliotecas/arquivos aula 2 (pandas)/" + nome + ".csv"
    df = pd.read_csv(nome)
    print(df)
    return df

estudantes = ler_csv("students_complete")
escolas = ler_csv("schools_complete") 
school_data_complete = pd.merge(estudantes,escolas,how="left",on=["school_name"]) # how --> método de mesclar; on --> coluna chave para a mescla

#unir em um dataframe school name e math score e school name com budget

per_school_math_score = school_data_complete.groupby(["school_name"])["math_score"].mean() #dentro de school data complete, agrupe os resultados por school name
#e me dê de retorno o dado da math score mas a média de math score.

per_school_reading_score = school_data_complete.groupby(["school_name"])["reading_score"].mean()
per_school_budget = school_data_complete.groupby(["school_name"])["budget"].mean()

print(per_school_budget.info())
print(per_school_math_score.info())
print(per_school_reading_score.info())

print(per_school_budget)
print(per_school_math_score)
print(per_school_reading_score)

#importante: quando voce faz uma operação como essa, a classe do objeto criado é um "pandas.core.series.series", ou seja,
# é uma série de dados, não um dataframe. para virar um dataframe, é preciso converter série para dataframe

per_school_math_score = per_school_math_score.to_frame().reset_index()
per_school_reading_score = per_school_reading_score.to_frame().reset_index()
per_school_budget = per_school_budget.to_frame().reset_index()

#quando mexemos com o groupby, o school name foi convertido em um index. assim, ele não é um dado no dataframe, mas um index.

#eu posso resolver isso usando o reset_index(). a necessidade disso é que precisamos pegar as vezes alguns dados em coluna
#e quando uma coluna vira um index é dificil de acessar esse dado.
#sem isso, a coluna do groupby (no caso, school name) se tornará a coluna índice

print(per_school_budget.info())
print(per_school_math_score.info())
print(per_school_reading_score.info())

print(per_school_budget)
print(per_school_math_score)
print(per_school_reading_score)

#correlacionar os dois dfs mantendo todas as colunas

school_data_math = pd.merge(per_school_budget,per_school_math_score, how="left",on=["school_name"])
school_data_reading = pd.merge(per_school_budget,per_school_reading_score, how="left",on=["school_name"])

print(school_data_reading)

#mostrar gráficos