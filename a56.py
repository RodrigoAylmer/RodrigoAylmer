'''
arquivo com somente as variáveis criadas nas aulas de 5 a 6, para importar na aula 7. esse arquivo é igual ao aula5_6_pandas_streamit.py
com a exceção de que esse não tem prints, apenas as variáveis

'''

import pandas as pd #importante gerar um apelido que simplifique a escrita do código
import numpy as np 

def ler_csv(nome):
    nome = "C:/Users/rdy/OneDrive - Danske Commodities/Danske/Python/Motim/Bibliotecas/arquivos aula 2 (pandas)/" + nome + ".csv"
    df = pd.read_csv(nome)
    print(df)
    return df

estudantes = ler_csv("students_complete")
escolas = ler_csv("schools_complete") 
school_data_complete = pd.merge(estudantes,escolas,how="left",on=["school_name"]) 
per_school_math_score = school_data_complete.groupby(["school_name"])["math_score"].mean() 
per_school_reading_score = school_data_complete.groupby(["school_name"])["reading_score"].mean()
per_school_budget = school_data_complete.groupby(["school_name"])["budget"].mean()
per_school_math_score = per_school_math_score.to_frame().reset_index()
per_school_reading_score = per_school_reading_score.to_frame().reset_index()
per_school_budget = per_school_budget.to_frame().reset_index()
school_data_math = pd.merge(per_school_budget,per_school_math_score, how="left",on=["school_name"])
school_data_reading = pd.merge(per_school_budget,per_school_reading_score, how="left",on=["school_name"])
