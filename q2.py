import matplotlib.pyplot as plt
import pandas as pd
dadosq2 = pd.read_csv('https://raw.githubusercontent.com/androidpcguy/bggn213/master/class05/bimm143_05_rstats/feature_counts.txt', delimiter = '\t')
plt.barh(dadosq2['Feature'], dadosq2['Count'])
plt.xlabel('Número de características')
plt.xticks([0,20000,40000,60000])
plt.show()

