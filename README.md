# Academic
Deposit of small scrypts used to facilitate the Academic Investigation. 

# Python Scripts for Keyword Extraction and Analysis on Newspaper Images

These 7 Python scripts were used in a research project focused on obtaining the frequency of keywords and their analysis present in images, if recognized as text, from a 1939 newspaper edition. Using these scripts, it was possible to create an Excel file with two columns: the first containing the image name, and the second containing the extracted text. This automation enabled the extraction of text from over 1000 images in about an hour on a low-end computer.

Subsequently, keyword extraction was performed in the same file. The next step involved counting the keywords and their total frequency in the images. This action required populating a table with approximately 90,000 entries (number of images x number of keywords), a task impossible for a researcher to do manually, but achieved in seconds.

Finally, it was possible to extract the 20 characters before and after each keyword, apply a Portuguese filter to identify nonexistent words, and obtain context clouds for each keyword. In this way, we have an open set of tools that allows researchers dealing with large image databases to extract and index keywords and even analyze their evolution in quartiles.

These 7 Python scripts were used in a research project focused on obtaining the frequency of keywords and their analysis present in images, if recognized as text, from a 1939 newspaper edition. Using these scripts, it was possible to create an Excel file with two columns: the first containing the image name, and the second containing the extracted text. This automation enabled the extraction of text from over 1000 images in about an hour on a low-end computer.

The following files are part of this project:

1. **Extrair OCR de Pasta de Imagens e Gravacao em Excel.py**
   - Uploaded to extract OCR from a folder of images and save it in an Excel file.

2. **FILTRAR RESULTADOS BELIGERANTES.py**
   - Uploaded to filter belligerent results.

3.1. **Contar Palavras-Chave _ valores boleanos.py**
   - Uploaded to count keywords with boolean values.

3.2. **Contar palavras-chave _frequencia.py**
   - Uploaded to count keywords and their frequency.

4.1. **Fazer contagem trimestral _ partindo do boleano _ em quantas folhas aparecem.py**
   - Uploaded to perform quarterly counting based on boolean values and determine the number of sheets.

4.2. **encontrar frequencia  palavras por folhas de jornal e trimestre.py**
   - Uploaded to find the frequency of words per newspaper sheet and quarter.

5. **Encontrar_contexto_das_palavras_chave.py**
   - Uploaded to find the context of keywords.

6. **gerar_nuvem_de_palavras.py**
   - Uploaded to generate word clouds.

In this way, we have an open set of tools that allows researchers dealing with large image databases to extract and index keywords and even analyze their evolution in quartiles.


I am not a programmer, so you are encouraged to use and enhance these scripts, which proved useful in the current investigation, "The Neutrality of Portugal in World War II," presented by Pedro Horta, and may be beneficial to others.

