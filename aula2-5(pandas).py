'''
Streamit - Biblioteca para fazer site
Jungle - biblioteca maior para sites, mas é mais trabalhosa

pip install -- comando para baixar

pip freeze -- mostra todas as bibliotecas baixadas no python e versões


se o pip não funcionar, é preciso instalar ele nas variáveis de ambiente
'''

'''
PANDAS: analisa dados simples e complexo.

Para que serve? Análise de dados

principais funções? filtrar, buscar, calcular médias...

O que ele lê? CSV, HTML, EXCEL, SQL e Json (orientação de objeto de Java)

Como lê?

read_csv, read_excel, read_sql...

'''


'''
df.head() --> top rows
df.tail() --> bottom rows
df.index --> mostra o index
df.columns --> mostra as colunas
df.T --> transpõe os dados
df.to_numpy() --> representa o df em numpy (uma matriz)
df.describe() --> descrição rápida dos dados. resumo estatístico:
    count
    mean
    std (desvio padrão)
    mín
    25%
    50%
    75%
    máx
df.info() --> descrição de informações do dataframe, inlcuindo:
    nomes das colunas
    valores não nulos
    data type de cada coluna e agregado
    uso da memória
df.sort_values(by, axis, ascending, inplace, kind, na_position) --> organiza os dados por valores
df.copy() --> cria uma copia do df
df.apply(função, eixo onde a função será aplicada)
df.dropna(how=como) --> remove valores faltantes
df.fillna(value=valor) --> preenche os NA/ NaN usando um método específico
df.replace(o que quero substituir, pelo quê vou substituir)
df.merge(right, how, on, left_on,right_on,left_index,right_index,sort,suffixes,copy,indicator,validate) --> fusiona dataframes no estilo join
df.join(other,on,how, Isuffix,rsuffix,sort) --> junta colunas de um outro dataframe
df.groupby(agrupar pelo que?) --> agrupa valores
df.pivot(index,columns,values) --> cria uma tabela pivô com base em valores de coluna
df.at[nome das linhas, nome das colunas] =  valor a ser definido --> estabelece valores pelos nomes
df.iat[índice das linhas, índice das colunas] = valor a ser estabelecido --> por índice


operações estatísticas:

df.mean() --> média para cada coluna
df.mean(axis=eixo) --> média para cada linha

funções definidas pelo usuário:

df.agg(função) --> reduz o resultado à agregados
df.transform(função)

df.value_counts() --> irá contar quantas vezes aparecem os valores na especificidade deles. o resultado será
    coluna de valores    coluna de quantas vezes eles aparecem


string methods


'''

import pandas as pd #importante gerar um apelido que simplifique a escrita do código
import numpy as np 
df = pd.read_csv("C:/Users/rdy/OneDrive - Danske Commodities/Danske/Python/Motim/Bibliotecas/arquivos aula 2 (pandas)/students_complete.csv")

print(df)

#mas eu posso estabelecer uma função para ler arquivos ao invés de fazer uma leitura direta. economiza código

def ler_csv(nome):
    nome = "C:/Users/rdy/OneDrive - Danske Commodities/Danske/Python/Motim/Bibliotecas/arquivos aula 2 (pandas)/" + nome + ".csv"
    df = pd.read_csv(nome)
    print(df)
    return df

estudantes = ler_csv("students_complete")

estudantes.describe()


#a vantagem de fazer isso é que eu posso fazer uma leitura mais rápida de outros arquivos, como por exemplo das escolas


escolas = ler_csv("schools_complete") # já lê corretamente o arquivo escolas

#qual a quantidade de alunos na minha base de estudantes?


print(estudantes.shape) # df.shape --> gera uma tupla com o número de linhas e colunas de um df.  (linhas, colunas)
print(estudantes.shape[0]) # mostra o primeiro elemento da tupla. como cada linha equivale a um aluno,
#basta eu imprimir a quantidade de linhas para saber quantos alunos há
total_estudantes = estudantes.shape[0]
#qual o orçamento geral para as escolas?

#R: o orçamento individual está nas colunas, então basta somente somar todos os valores da coluna de orçamento individual

orcamento_total = escolas["budget"].sum() # dentro de escolas, busque a coluna "budget" e aplique o método sum()

print(f"O orçamento total das escolas é US$ {orcamento_total}")

#Qual são as médias das notas de math e reading dos alunos?

avg_math = estudantes["math_score"].mean()

print(f"Média dos alunos em matemática: {avg_math:.0f}")
avg_reading = estudantes["reading_score"].mean()

print(f"Média dos alunos em leitura: {avg_reading:.0f}")

#qual a porcentagem de alunos aprovados em matemática, sendo a média 70?

aprovados_math = estudantes.loc[estudantes["math_score"]>70].count() # df estudantes --> método loc --> identifica as coisas com base em alguma condição
# método count() --> conta os argumentos. 

print(aprovados_math) # isso imprime a quantidade de colunas que satisfazem as condições. dá vários resultados, pra cada coluna

#se eu quero somente de uma coluna, eu posso especificar ela no final

aprovados_math = estudantes.loc[estudantes["math_score"]>70].count()["student_name"] # especificar a coluna student_name

print(aprovados_math)

porcentagem_math = (aprovados_math/(estudantes["student_name"].count()))*100

print(f"Foram aprovados {porcentagem_math:.2f}% do total de alunos em matemática")

#criar um dataframe que combine as informações dos 2 dataframes já fornecidos
#R: é necessário ter alguma coisa em comum para juntar os dataframes. nesse caso, o nome da escola é a coluna de interseção entre eles

school_data_complete = pd.merge(estudantes,escolas,how="left",on=["school_name"]) # how --> método de mesclar; on --> coluna chave para a mescla

print(school_data_complete.columns)



#calcule a porcentagem de alunos aprovados tanto em reading como em math

pass_math_reading_count = school_data_complete[(school_data_complete["math_score"]>=70) & (school_data_complete["reading_score"]>=70)].count()["student_name"]

'''
Estrutura acima:

dentro de school_data_complete, eu quero filtrar os dados que sejam tanto maiores que 70 na coluna "math score"
quanto maiores que 70 na coluna "reading score". nesse caso, encontrando esses dois dados, aplique o método count() na coluna "student name".

nota:  o "&" aplica duas condições ao mesmo tempo
'''

print(f"Aprovados nas duas matérias: {pass_math_reading_count}")


#crie um df que dê uma visão geral do total de cada campo como orçamento, estudante e porcentagem de aprovação

numero_estudantes = school_data_complete["student_name"].count()
numero_escolas = school_data_complete["school_name"].nunique() # busca a quantidade de valores únicos e unique() mostra os valores únicos

orcamento_total = school_data_complete["budget"].unique().sum() #unique() encontra os valores únicos e sum() soma eles
orcamento_medio = school_data_complete["budget"].unique().mean() #média

media_math = school_data_complete["math_score"].mean()
media_reading = school_data_complete["reading_score"].mean()


#criando o resumo dos dados

resumo = pd.DataFrame({
        "Numero de estudantes": numero_estudantes,
        "Numero escolas": numero_escolas,
        "Orçamento médio": orcamento_medio,
        "Orçamento total": orcamento_total,
        "Media em matemática": media_math,
        "Media leitura": media_reading
    },index=[0])

print(resumo)

