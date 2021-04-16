import matplotlib.pyplot as plt
import pandas as pd
dadosq4 = pd.read_csv('https://raw.githubusercontent.com/androidpcguy/bggn213/master/class05/bimm143_05_rstats/male_female_counts.txt', delimiter = '\t')

plt.bar(dadosq4['Sample'], dadosq4['Count'], color= ['red','orange', 'yellow', 'lime', 'springgreen', 'cyan', 'dodgerblue', 'purple','deeppink','fuchsia'])
plt.yticks([0, 5, 10, 15])
plt.show()