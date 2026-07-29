import os
import pdfplumber

pasta = "C:/Users/bruno/Desktop/MAGALU 5240 69  5235 98"

arquivos = os.listdir(pasta)

pdf = [arquivo for arquivo in arquivos if arquivo.endswith(".pdf")]


def extrair_texto(pasta, pdf):
    """
    :param pasta: pasta dos arquivos
    :param pdf: pdf ou listas de pdfs
    :return:
    """
    pdf_aberto = pdfplumber.open(f"{pasta}/{pdf}")

    primera_pagina = pdf_aberto.pages[0]
    texto_extraido_pagina_um = primera_pagina.extract_text()

    if texto_extraido_pagina_um is None or texto_extraido_pagina_um == "":
        print(f"⚠️ não consegui ler esse PDF ({pdf}), provavelmente é imagem")
    else:
        return texto_extraido_pagina_um

documentos_obrigatorios = {
    "transferencia_pf": ["cnh", "Comprovante_de_endereco", "Extrato_bancario", "imposto_de_Renda_PF", "Certidao_de_estado_civil"],

    "transferencia_pj": ["cnh", "Comprovante_de_endereco_da_empresa", "Certidao_de_estado_civil", "Contrato_social", "Simples_Nacional",  "Renda_da_empresa"],
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

def definir_tipo_docoumento(texto_extrido_documento):
    candidato = []
    resultados = {}

    for tipo_documento, palavra_chave in palavras_chaves.items():
        for palavra in palavra_chave:
            if palavra in texto_extrido_documento.lower():
                candidato.append(tipo_documento)
                break

    return candidato


resultados = {}

for arquivo in pdf:
    texto = extrair_texto(pasta, arquivo)
    if texto is None:
        resultados[arquivo] = [f"Precisa analisar Manualmente"]
    else:
        resultados[arquivo] = definir_tipo_docoumento(texto)

print(resultados)


def difinir_tipo_cadastro(resultados):

    if any("Contrato_social" in lista_documentos for lista_documentos in resultados.values()):
        return "transferencia_pj"
    else:
        return "transferencia_pf"

print(difinir_tipo_cadastro(resultados))


documentos_encontrados = []

for lista_documentos in resultados.values():
    documentos_encontrados.extend(lista_documentos)

print(documentos_encontrados)

documentos_faltando = []

for documento in documentos_obrigatorios[difinir_tipo_cadastro(resultados)]:
    if documento not in documentos_encontrados:
        documentos_faltando.append(documento)

if (len(documentos_faltando) > 0):
    print(f"Segue a lista de documentos que faltam: {documentos_faltando}")

else:
    print("Todos docuemntos encontrados")