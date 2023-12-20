import os
import cv2
import pytesseract
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

# Configuração do Tesseract (caminho para o executável do Tesseract)
pytesseract.pytesseract.tesseract_cmd = r'D:\python instal\tesseract_ocr\tesseract.exe'

# Função para processar a pasta selecionada
def processar_pasta():
    pasta_entrada = filedialog.askdirectory(title="Selecione a Pasta de Entrada")
    pasta_saida = filedialog.askdirectory(title="Selecione a Pasta de Saída")

    # Lista para armazenar os resultados
    resultados = []

    # Obter a quantidade total de imagens na pasta de entrada
    total_imagens = len([nome_arquivo for nome_arquivo in os.listdir(pasta_entrada)
                         if nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.png')])

    # Configurar a barra de progresso
    barra_progresso['maximum'] = total_imagens
    barra_progresso['value'] = 0

    # Loop para processar cada imagem na pasta de entrada
    for i, nome_arquivo in enumerate(os.listdir(pasta_entrada)):
        if nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.png'):
            # Atualizar a barra de progresso
            barra_progresso['value'] = i + 1
            root.update_idletasks()  # Atualizar a interface gráfica

            # Caminho completo do arquivo de entrada
            caminho_arquivo_entrada = os.path.join(pasta_entrada, nome_arquivo)

            # Caminho completo do arquivo de saída na pasta "editados"
            caminho_arquivo_editado = os.path.join(pasta_saida, nome_arquivo)

            # Leitura da imagem usando OpenCV em escala de cinza
            imagem = cv2.imread(caminho_arquivo_entrada, cv2.IMREAD_GRAYSCALE)

            # Realizar OCR na imagem pré-processada
            texto_extraido = pytesseract.image_to_string(imagem, lang='por')

            # Adicionar resultados à lista
            resultados.append({'Nome do Arquivo': nome_arquivo, 'Texto Extraído': texto_extraido})

    # Criar um DataFrame do pandas a partir da lista de resultados
    dados = pd.DataFrame(resultados)

    # Salvar os resultados em um arquivo Excel dentro da pasta "editados"
    caminho_excel = os.path.join(pasta_saida, '1.resultados_ocr_sem edicao.xlsx')
    dados.to_excel(caminho_excel, index=False, engine='openpyxl')

    print(f'Imagens editadas e resultados salvos em {caminho_excel}')

# Configuração da interface gráfica
root = Tk()
root.title("Extractor de OCR")

# Botão para iniciar o processamento
btn_processar = Button(root, text="Inciar Processamento OCR de Pasta", command=processar_pasta)
btn_processar.pack(pady=20)

# Barra de progresso
barra_progresso = ttk.Progressbar(root, length=300, mode='determinate')
barra_progresso.pack(pady=10)

# Iniciar a interface gráfica
root.mainloop()
