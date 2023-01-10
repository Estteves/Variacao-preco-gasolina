import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

grafico = pd.read_csv('gasolina.csv')
display(grafico)

grafico_linha = sns.lineplot(data = grafico, x = 'dia', y='venda', color='red')
grafico_linha.set_title("Preço da gasolina por dia")
plt.savefig('gasolina.png')
plt.show()