# Importando as bibliotecas necessárias
import pandas as pd
# Leitura do arquivo Excel. Pode-se igualmente fazer um input.
df = pd.read_excel('1.resultados_ocr_sem edicao.xlsx')
# Lista para armazenar os índices das linhas encontradas
indices_encontrados = []
# Palavras-chave a serem encontradas. Pode-se subsituir por um input.
palavras_chave = [
    "australia", "austrália", "canadá", "churchill", "frança", "inglaterra", "ingles",
    "inglês", "reino unido", "sul-africana", "união sul-africana", "alemanha",
    "alemao", "alemão", "chanceler", "ciano", "duce", "fuhrer", "germano", "hitler",
    
    "italia", "itália", "japão", "mussolini", "ribbe", "ribentropp", "checoslováquia",
    "austria", "boemia", "boémia", "checo", "checoslováquia", "eslovaca", "guerra",
    
    "beligerante", "combate", "conflito", "frente", "militar", "neutral", "neutralidade",
    "pacto", "ofensiva", "invasao", "invasão", "vitoria", "vitória", "derrota", "capitula",
    
    "capitulação", "capitularam", "retirada", "sião", "judaica", "judeu", "macon", "maçon",
    "maçonaria", "molotov", "siao", "soviética", "ouro", "espanha", "franco", "salazar",
    
    "polónia", "danzig", "polonia", "varsovia", "varsóvia", "estados unidos", "andorra",
    "argentina", "belgica", "bélgica", "china", "dinamarca", "finlandia", "holanda",
    
    "irlanda", "saudita", "suecia", "suécia", "suica", "suiça"


]
# Iteração sobre cada linha do DataFrame
for index, row in df.iterrows():
    # Iteração sobre cada palavra-chave
    for palavra in palavras_chave:
        # Verifica se a palavra-chave está presente na segunda coluna (índice 1)
        if palavra.lower() in str(row[1]).lower():
            # Adiciona o índice da linha à lista
            indices_encontrados.append(index)
            # Adiciona a palavra-chave como coluna e sinaliza com 'x'
            df.loc[index, palavra] = 'x'
# Preenche valores nulos nas novas colunas com ''
df.fillna('', inplace=True)
# Filtra o DataFrame mantendo apenas as linhas encontradas
df_filtrado = df.loc[indices_encontrados]
# Remove linhas duplicadas do DataFrame filtrado
df_filtrado = df_filtrado.drop_duplicates()
# Salva o DataFrame de resultados em um novo arquivo Excel
df_filtrado.to_excel('2.Palavras_chave_beligerantes.xlsx', index=False)







