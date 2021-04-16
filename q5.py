import matplotlib.pyplot as plt 
import pandas as pd
#Lê a base de dados direto do github
dadosq5 = pd.read_csv('https://raw.githubusercontent.com/androidpcguy/bggn213/master/class05/bimm143_05_rstats/up_down_expression.txt', delimiter = '\t')
#Defino variaveis para as colunas e valores que eu desejo, as variaveis cima, baixo e inalterado especificam que eu quero buscar os valores, "up", "down" e "unchanging" especificamente na coluna State do banco de dados, Condition1 recebe a coluna Condition1 e a outra variável recebe condition2
cima = dadosq5[dadosq5.State == "up"]
baixo = dadosq5[dadosq5.State == "down"]
inalterado = dadosq5[dadosq5.State == "unchanging"]
Condition1 = dadosq5['Condition1']
Condition2 = dadosq5['Condition2']
#Defino o plot como tipo Scatter e quero no eixo X os valores que o State é "up" na coluna Condition1 e o eixo Y são os valores que são "up" na coluna condition2 e depois defino a cor como C = "r" e "r" é igual a red = vermelho
plt.scatter(cima.Condition1, cima.Condition2, c = 'r')
#Defino o plot como tipo Scatter e quero no eixo X os valores que o State é "down" na coluna Condition1 e o eixo Y são os valores que são "down" na coluna condition2 e depois defino a cor como C = "blue"  blue = Vermelho
plt.scatter(baixo.Condition1, baixo.Condition2, c = 'blue')
#Defino o plot como tipo Scatter e quero no eixo X os valores que o State é "unchanging" na coluna Condition1 e o eixo Y são os valores que são "unchanging" na coluna condition2 e depois defino a cor como C = "gray" e gray = cinza
plt.scatter(inalterado.Condition1, inalterado.Condition2, c = "gray")
#Definindo caracteristicas do gráfico
plt.ylabel('Condição2')
plt.yticks([0,5,10])
plt.xlabel('Condição1')
plt.xticks([0,5,10])
plt.show()