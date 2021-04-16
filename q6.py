import matplotlib.pyplot as plt 
import pandas as pd
#Lê a base de dados direto do github
dadosq6 = pd.read_csv('https://raw.githubusercontent.com/androidpcguy/bggn213/master/class05/bimm143_05_rstats/chromosome_position_data.txt', delimiter = '\t')
#Plots do tipo normal, ou seja, linha e definindo os valores de x e y especificamente e defindo as cores e quando coloco label quero dizer que quero que apareça no gráfico como legenda
plt.plot(dadosq6['Position'], dadosq6['Mut1'], c = 'r', label = 'Mut1')
plt.plot(dadosq6['Position'], dadosq6['Mut2'], c = 'blue', label = 'Mut2')
plt.plot(dadosq6['Position'], dadosq6['WT'], c = 'green', label = 'WT')
#Definindo caracteristicas do gráfico
plt.xlabel('posição dentro dos cromossomos')
plt.ylabel('Valores')
plt.yticks([0,10,20,30,40,50,60,70])
#Esse legend é para definir o local onde vai ficar a legenda, nesse caso, eu escolhi upper left é que o canto superior esquerdo do gráfico.
plt.legend(loc = 'upper left')
plt.show()