import matplotlib.pyplot as plt
import pandas as pd

dadosq1 = pd.read_csv('https://raw.githubusercontent.com/androidpcguy/bggn213/master/class05/bimm143_05_rstats/weight_chart.txt', delimiter = '\t')

plt.plot(dadosq1['Age'], dadosq1['Weight'], 'o')
plt.plot(dadosq1['Age'], dadosq1['Weight'])
plt.xlabel('Idade(Meses)')
plt.ylabel('Peso(Kg)')
plt.title('A relação entre idade e peso em um bebê em crescimento')
plt.show()