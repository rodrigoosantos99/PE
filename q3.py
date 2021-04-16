import matplotlib.pyplot as plt
import numpy as np
#Crio 3 váriveis, 2 para receber os diferentes plots e uma para concatenação, no plot1 eu crio um gráfico com valor de destribuição normal com o valor 10000, no plot 2 eu creio uma varíavel e utilizo loc = 4 para ir 4 espações para o lado de onda normalmente ficaria e no plot3 eu uso a concatenação dos plots.
plot1 = np.random.normal(size = 10000)
plot2 = np.random.normal(loc=4, size = 10000)
plot3 = np.concatenate((plot1,plot2))
#Definindo que quero plotar como histograma, bins é um número de barras que desejo para representar, histtype é o tipo, color é cor e ec é borda
plt.hist(plot3, bins=170, histtype='bar', color='white', ec='black')
#Definindo caractéristicas do gráfico
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.yticks([0,100,200,300,400])
plt.show()