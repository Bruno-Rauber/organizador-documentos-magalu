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

documentos_obrigatorios = {
    "transferencia_pf": ["cnh", "Comprovante_de_endereco", "Extrato_bancario", "imposto_de_Renda_PF", "Certidao_de_estado_civil"],

    "transferencia_pj": ["cnh", "Comprovante_de_endereco", "Certidao_de_estado_civil", "Contrato_social", "Simples_Nacional", "Comprovante_de_endereco_da_empresa", "Renda_de_empresa"],

    "concessao": ["Fotos_do_veiculo", "CRLV"]
}

