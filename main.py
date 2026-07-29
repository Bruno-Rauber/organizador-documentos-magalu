import os
import pdfplumber

pasta = "C:/Users/bruno/Desktop/MAGALU 5240 69  5235 98"

arquivos = os.listdir(pasta)

pdf = [arquivo for arquivo in arquivos if arquivo.endswith(".pdf")]

print(pdf)

def extrair_texto(pasta, pdf):
    pdf_aberto = pdfplumber.open(f"{pasta}/{pdf}")

    primera_pagina = pdf_aberto.pages[0]
    texto_extraido_pagina_um = primera_pagina.extract_text()

    if texto_extraido_pagina_um is None or texto_extraido_pagina_um == "":
        print("⚠️ não consegui ler esse PDF, provavelmente é imagem")
    else:
        return texto_extraido_pagina_um

print(extrair_texto(pasta, pdf[0]))