import pandas as pd

# Leitura do arquivo Excel
df = pd.read_excel('1.resultados_ocr_sem edicao.xlsx')

# Palavras-chave a serem buscadas
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

# Criar colunas para cada palavra-chave e inicializar com zero
for palavra in palavras_chave:
    df[palavra] = 0

# Iteração sobre cada linha do DataFrame
for index, row in df.iterrows():
    # Iteração sobre cada palavra-chave
    for palavra in palavras_chave:
        # Contar a quantidade de vezes que a palavra-chave aparece
        df.loc[index, palavra] = str(row[1]).lower().count(palavra.lower())

# Salva o DataFrame de resultados em um novo arquivo Excel
df.to_excel('2.1 Palavras_chave_contagem de repeticoes.xlsx', index=False)
