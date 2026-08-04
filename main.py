import os
import pdfplumber

pasta_para_analise_arquivos = "C:/Users/bruno/Desktop/pasta para teste de codigo"

lista_todos_arquivos = os.listdir(pasta_para_analise_arquivos)

lista_pdfs = [arquivo for arquivo in lista_todos_arquivos if arquivo.endswith(".pdf")]

def extrair_texto(pasta: str, pdf: list) -> str:
    """
    Recebe uma pasta e um arquivo(PDF) dela para extrair
    o texto da primeira página
    """
    abrir_pdf = pdfplumber.open(f"{pasta}/{pdf}")

    primera_pagina = abrir_pdf.pages[0]
    texto_extraido_pagina_um = primera_pagina.extract_text()

    if texto_extraido_pagina_um is None or texto_extraido_pagina_um == "":
        print(f"⚠️ Não consegui ler esse PDF ({pdf}), provavelmente é uma imagem \n")
    else:
        return texto_extraido_pagina_um

documentos_obrigatorios = {
    "transferencia_pf": ["cnh", "Comprovante_de_endereco", "Extrato_bancario", "imposto_de_Renda_PF", "Certidao_de_estado_civil"],

    "transferencia_pj": ["cnh", "Comprovante_de_endereco_da_empresa", "Comprovante_de_endereco", "Certidao_de_estado_civil", "Contrato_social", "Simples_Nacional",  "Renda_da_empresa"],
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

def definir_tipo_documento(texto_extraido_pagina_um: str) -> list:
    """
    Recebe o texto extraído da priemira página de um PDF
    para definir o tipo de documento ele é
    com base em palavras chaves
    """
    candidato = []

    for documento, palavras in palavras_chaves.items():
        for palavra in palavras:
            if palavra in texto_extraido_pagina_um.lower():
                candidato.append(documento)
                break

    return candidato

def executar_pasta(lista_pdfs: list) -> dict:
    resultados = {}  # Resultados é Dic onde cada chave é o Nome original do arquivo e o valor é o possivel tipo de arquivo que ele é

    for pdf in lista_pdfs:
        texto = extrair_texto(pasta_para_analise_arquivos, pdf)
        if texto is None:
            resultados[pdf] = [f" ({pdf}) Sem identeificação"]
        else:
            resultados[pdf] = definir_tipo_documento(texto)
    return resultados

loop_da_pasta = executar_pasta(lista_pdfs) # Essa variável guarda a chamada da função que percorre a pasta em questão

def definir_tipo_cadastro(resultados: dict) -> str:

    if any("Contrato_social" in lista_documentos for lista_documentos in resultados.values()):
        return "transferencia_pj"
    else:
        return "transferencia_pf"


documentos_encontrados = []

for lista_documentos in loop_da_pasta.values():
    documentos_encontrados.extend(lista_documentos)

print(f"Documentos encontrado são {documentos_encontrados} \n")

documentos_faltando = []

for documento in documentos_obrigatorios[definir_tipo_cadastro(loop_da_pasta)]:
    if documento not in documentos_encontrados:
        documentos_faltando.append(documento)

if (len(documentos_faltando) > 0):
    print(f"Segue a lista de documentos que faltam: {documentos_faltando}")

else:
    print("Todos documentos encontrados")
