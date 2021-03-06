# Código de geração do gráfico de linhas

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

# Transformação do arquivo CSV para um DataFrame
gasolina_df = pd.read_csv('gasolina.csv', delimiter=',')

# Criação do gráfico de linha
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='dark')
  grafico.set(title='Gas price averages between July 1 and July 10, 2021', xlabel='Day', ylabel='Price (BRL)')
  grafico.figure.set_size_inches(w=30/2.54, h=20/2.54)

# Salvando o gráfico em PNG
grafico.figure.savefig(fname='gasolina.png', bbox_inches='tight')