#Quando o ficheiro de analise contem (e acontece), valores zero na coluna context
#este programa dá erro. Uma solução será filtrar os resultados e aagar os zeros
#ou melhorar o scrypt criando um filtro


##GERAR NUVEM DE PALAVRAS

# Importando as bibliotecas necessárias
import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Obtém todas as palavras em português do dicionário
with open('dic.txt', 'r', encoding='utf-8') as file:
    palavras_em_portugues = set(file.read().split())


# Leitura do arquivo Excel original
df_contexto = pd.read_excel('4.contexto_palavras_encontradas.xlsx')

# Obter palavras-chave da primeira coluna e remover duplicatas
palavras_chave = df_contexto.iloc[:, 0].unique()

# Função para gerar nuvem de palavras
def gerar_nuvem_palavras(texto, palavra_chave):
    # Configurações da nuvem de palavras
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto)

    # Plotagem da nuvem de palavras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Nuvem de Palavras para "{palavra_chave}"')
    plt.axis('off')
    plt.show()


# Iteração sobre cada palavra-chave
for palavra in palavras_chave:
    # Filtrar textos relevantes para a palavra-chave (substitua 'df_contexto' pelo seu DataFrame)
    textos_relacionados = df_contexto[df_contexto['Contexto'].str.contains(palavra, case=False)]['Contexto'].str.cat(sep=' ')

    # Remover palavras truncadas e símbolos
    textos_filtrados = re.sub(r'\b\w{1,2}\b|\W', ' ', textos_relacionados)

    # Filtrar palavras em português

    palavras_filtradas = [palavra for palavra in textos_filtrados.split() if palavra.lower() in palavras_em_portugues]

    # Juntar as palavras filtradas de volta em um texto
    texto_final = ' '.join(palavras_filtradas)

    if palavras_filtradas:
        # Configurações da nuvem de palavras para gravar e não exibir
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_final)

         # Salvar a nuvem de palavras com o nome da palavra
        wordcloud.to_file(f"{palavra}_nuvem_palavras.png")
        
        # Gerar nuvem de palavras - caso se queira exibir
        #gerar_nuvem_palavras(texto_final, palavra)
    else:
        # Se não houver palavras, mostrar mensagem
        print(f"Nada encontrado para a palavra-chave: {palavra}")



