# Anotações segunda aula de python intensivo

# Utilizar o python para análise de dados e base de dados
# Churn: cancelar sua assinatura que você vem pagando
# Sempre começar um projeto descrevendo os passos em portugues
# Análise de dados (Top-down) : 1° Análise Global/Inicial , 2° Análise Detalhada
# .map("{:.1%}.format") Esse comando formata os valores para porcentagem com 1 casa decimal

# Bibliotecas: import plotly.express as px (Construir gráficos em python)

# SEMPRE QUE TRABALHAR COM DADOS UTILIZAR A BIBLIOTECA PANDAS (import pandas as pd)

# Em análise de dados o que não te ajuda te atrapalha !

# Comandos pandas: variaveltabela = variavel.drop("nome_de_quem_voce_vai_jogar_fora", axis = 0 (linha) ou 1(coluna)) // (["Para deletar mais de uma coluna ou linha colocar colchetes"])
#                  tabela["Nome_coluna"] = pd to_numeric(tabela["Nome_coluna"], errors = "coerce") (Esse comando faz trocar o formato em que uma coluna está sendo lida, no exemplo trocar o formato para numeric, e se houver informações que não podem ser trocadas colocar "coerce" que faz a informação ficar vazia(NaN))
#                  print(tabela["Churn"].value_count()) (Esse comando vai contar os valores da coluna Churn) (.value_count(normalize = True) esse comando vai trazer os valores em porcentagem) 


# Tratamento de dados:
# 1° Analisar se o python está lendo as informações no formato correto
# Como faz?: print(tabela.info) mostra formato que as informações estão sendo lidas
# 2° Será que existe alguma coluna completamente vazia? (NaN em python é vazio)
# Como faz?: tabela = tabela.dropna(how="all", axis= 1) (Comando especial que exclui todas as colunas que são completamente vazia)
# 3° Será que existem alguma linha com informação vazia?
# Como faz?: tabela = tabela.dropna(how="any", axis= 0) (Comando especial que exclui as linhas onde pelo meno ha uma informação vazia)

# Comandos plotly:  grafico = px.histogram(tabela, x = "nome coluna" ) Esse comando constroi graficos 
#                   grafico.show() Esse comando mostra os graficos construidos