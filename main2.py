import os
import pdfplumber

pasta_para_analise_arquivos = "C:/Users/bruno/Desktop/pasta para teste de codigo"

lista_todos_arquivos = os.listdir(pasta_para_analise_arquivos)

lista_pdfs = [arquivo for arquivo in lista_todos_arquivos if arquivo.endswith(".pdf")]


def executar_pasta(pasta, lista_pdfs):

    documentos_obrigatorios = {
        "transferencia_pf": ["cnh", "Comprovante_de_endereco", "Extrato_bancario", "imposto_de_Renda_PF",
                             "Certidao_de_estado_civil"],

        "transferencia_pj": ["cnh", "Comprovante_de_endereco_da_empresa", "Comprovante_de_endereco",
                             "Certidao_de_estado_civil", "Contrato_social", "Simples_Nacional", "Renda_da_empresa"],
    }

    palavras_chaves = {
        "cnh": ["senatran"],
        "Comprovante_de_endereco": ["sanepar", "copel", "cep", "endereço"],
        "Extrato_bancario": ["extrato", "agência"],
        "imposto_de_Renda_PF": ["imposto de renda"],
        "Certidao_de_estado_civil": ["certidao de casamento", "certidao de nascimento"],
        "Contrato_social": ["contrato social"],
        "Simples_Nacional": ["simples nacional"],
        "Comprovante_de_endereco_da_empresa": ["sanepar", "copel", "cep"],
        "Renda_da_empresa": ["extrato", "agência"],
        "crlv": ["renavam"]
    }

    resultados_pdf = {}

    for pdf in lista_pdfs:
        abrir_pdf = pdfplumber.open(f"{pasta}/{pdf}")
        primera_pagina = abrir_pdf.pages[0]
        texto_extraido_pagina_um = primera_pagina.extract_text()

        if texto_extraido_pagina_um is None or texto_extraido_pagina_um == "":
            print(f"⚠️ não consegui ler esse PDF ({pdf}), provavelmente é imagem")
        else:
            for key, palavras in palavras_chaves.items():
                for palavra in palavras:
                    if palavra in texto_extraido_pagina_um.lower() and not key in resultados_pdf:
                     resultados_pdf.setdefault(pdf, []).append(key)
                    else:
                        continue

    print(resultados_pdf)


executar_pasta(pasta_para_analise_arquivos, lista_pdfs)

