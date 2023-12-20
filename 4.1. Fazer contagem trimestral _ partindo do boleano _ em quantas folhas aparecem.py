#obriga a fazer uma limpeza do ficheiro de origem. apagrar os falsos

#Eliminar a coluna do texto
#retirar o filtro

import pandas as pd

# Carregar o ficheiro Excel
caminho_ficheiro = '3.1.contagem_falso_verdadeiro.xlsx'
dados = pd.read_excel(caminho_ficheiro)

# Divisão em trimestres
total_linhas = len(dados)
linhas_por_trimestre = total_linhas // 4
print(total_linhas)

# Inicializar um novo DataFrame com colunas dinâmicas
colunas_dinamicas = ['Nome do Arquivo'] + list(dados.columns[1:])  # Excluir a primeira coluna, que é o título 'Período'
resultados = pd.DataFrame(columns=colunas_dinamicas)
print(resultados)

# Iterar pelos trimestres
for i in range(4):
    inicio = i * linhas_por_trimestre
    fim = (i + 1) * linhas_por_trimestre if i < 3 else total_linhas
    trimestre = f'Trimestre {i+1}'

    # Contar as linhas em que as palavras-chave não estão em branco
    contagens = dados.iloc[inicio:fim, 1:].apply(lambda coluna: coluna[coluna.notna()].count())

    # Adicionar resultados ao DataFrame
    resultados = pd.concat([resultados, pd.DataFrame({'Nome do Arquivo': trimestre, **contagens.to_dict()}, index=[0])], ignore_index=True)

# Guardar os resultados num novo ficheiro Excel
resultados.to_excel('3.3 contagem palavras chave absolutas por trimestre_em_bruto.xlsx', index=False)

