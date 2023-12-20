# Importando as bibliotecas necessárias
import pandas as pd
import re

# Obtém todas as palavras em português do dicionário
with open('dic.txt', 'r', encoding='utf-8') as file:
    palavras_em_portugues = set(file.read().split())



# Leitura do arquivo Excel original
df = pd.read_excel('2.Palavras_chave_beligerantes.xlsx')

# Lista para armazenar as palavras e seus contextos
dados_contexto = []


# Palavras-chave a serem buscadas (nomes das colunas a partir da terceira)
palavras_chave = df.columns[2:].tolist()

# Iteração sobre cada palavra-chave
for palavra in palavras_chave:
    # Coluna para armazenar os contextos
    df[palavra] = ''

    # Iteração sobre cada linha do DataFrame
    for index, row in df.iterrows():
        # Verifica se a palavra-chave está presente na segunda coluna (índice 1)
        if palavra.lower() in str(row[1]).lower():
            # Adiciona o contexto à lista de dados
            inicio = max(0, row[1].lower().find(palavra.lower()) - 20)
            fim = min(len(row[1]), row[1].lower().find(palavra.lower()) + len(palavra) + 20)
            contexto = row[1][inicio:fim]
            dados_contexto.append([palavra, contexto])

# Cria um novo DataFrame com os dados de contexto
df_contexto = pd.DataFrame(dados_contexto, columns=['Palavra', 'Contexto'])


# Salva o DataFrame de contexto em um segundo arquivo Excel
df_contexto.to_excel('4.contexto_palavras_encontradas.xlsx', index=False)
