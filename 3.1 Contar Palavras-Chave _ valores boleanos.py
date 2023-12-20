import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo Excel
df = pd.read_excel('2.Palavras_chave_beligerantes.xlsx')

# Exemplo de análise simples contando a presença de cada palavra-chave
palavras_chave = df.columns[2:]

# Ordenar o DataFrame pela contagem total
#df = df[palavras_chave].sum().sort_values(ascending=False)

for palavra in palavras_chave:
    df[palavra] = df['Texto Extraído'].str.contains(palavra, case=False)

df.to_excel('3.1.contagem_falso_verdadeiro.xlsx', index=False)

# Contagem absoluta de referências
contagem_referencias = df[palavras_chave].sum().sort_values(ascending=False)



# Criar uma figura e eixos
fig, ax = plt.subplots()

# Plotar dados nos eixos
contagem_referencias.plot(kind='bar', ax=ax, xlabel='Palavras-chave', ylabel='Contagem', title='Contagem Absoluta de Referências')

# Ajustar layout para garantir visibilidade das palavras
plt.tight_layout()

# Salvar a figura em um arquivo (por exemplo, em formato PNG)
plt.savefig('grafico_barras_contagem_palavras_chave.png')

# Se necessário, exibir o gráfico
plt.show()




# Salvar os resultados em um arquivo Excel dentro da pasta 
contagem_referencias.to_excel('3.contagem_numerica_total_palavras_chave_booleanos.xlsx', index=True)

