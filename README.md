# Organizador de Documentos de Cadastro (Magalu)

Script em Python que organiza, classifica e confere a documentação de clientes recebida para cadastro em um consórcio (Transferência de cota, pessoa física ou jurídica), automatizando uma tarefa que hoje é feita manualmente no dia a dia administrativo.

## O problema real

No fluxo de trabalho que uso (recebimento de documentos de clientes via WhatsApp e cadastro no sistema de consórcios), os arquivos chegam com nomes aleatórios (`1.pdf`, `IMG_20250727.pdf`, etc). Antes de lançar o cadastro no sistema, é preciso identificar manualmente cada documento, organizá-lo e conferir se toda a documentação obrigatória está presente — um trabalho repetitivo e sujeito a erro humano (esquecer de conferir um documento, por exemplo).

## O que o script faz

1. Lê todos os PDFs de uma pasta
2. Extrai o texto de cada arquivo (`pdfplumber`)
3. Classifica o tipo de cada documento por palavra-chave (CNH, comprovante de endereço, extrato bancário, contrato social, etc.)
4. Detecta arquivos ilegíveis (fotos/scans sem texto extraível) e sinaliza para conferência manual, em vez de travar ou assumir errado
5. Infere o tipo de cadastro (Transferência PF ou PJ) pela presença de "Contrato Social"
6. Confere quais documentos obrigatórios estão faltando, com base no tipo de cadastro identificado
7. Decide o nome final de cada documento — único candidato usa o nome identificado; casos ambíguos (ex: comprovante de endereço pessoal vs. da empresa, indistinguíveis por texto) ficam marcados como `Nao_identificado` para conferência manual; documentos duplicados do mesmo tipo (ex: múltiplos extratos) são numerados automaticamente
8. Renomeia os arquivos fisicamente na pasta

## O que fica de fora, conscientemente

Este projeto tem escopo definido com base em limitações técnicas reais, não por falta de tentativa:

- **Automação do sistema Magalu (preencher cadastro, anexar documentos):** exige automação de navegador (Playwright), que fica para uma próxima etapa do projeto, condicionada a mais base técnica.
- **Extração de nome/CPF do cliente:** o documento pessoal mais universal (CNH Digital do Detran) sempre chega como imagem, não texto extraível — os dados ficam em uma camada não acessível por `pdfplumber`. Resolver isso exigiria OCR e processamento de imagem, fora do escopo atual.
- **Diferenciação de comprovante de endereço pessoal vs. empresa:** ambos compartilham exatamente as mesmas palavras-chave (o conteúdo de uma conta de luz não muda entre pessoa física e empresa) — a única diferença real é o titular do documento, que esbarra na mesma limitação de imagem acima.
- **Concessão de crédito e fase 2 do cadastro (termo assinado):** fora do escopo definido para esta versão.

## Tecnologias

- Python 3
- `pdfplumber` — extração de texto de PDF
- `os` — manipulação de arquivos e pastas
- `collections.Counter` — numeração de documentos duplicados

## Como rodar

```bash
pip install -r requirements.txt
```

Ajuste o caminho da pasta na variável `pasta_para_analise_arquivos` em `main.py` e execute:

```bash
python main.py
```

## Uso de IA no desenvolvimento

Este projeto foi desenvolvido com apoio de IA (Claude) como ferramenta de mentoria — para validar viabilidade técnica, revisar lógica e sugerir sintaxe/bibliotecas Python. Todas as decisões de escopo, arquitetura e trade-offs (o que automatizar, o que deixar de fora e por quê, como tratar casos ambíguos) foram discutidas e definidas ao longo do processo, não geradas automaticamente.

## Aprendizados técnicos

- Leitura e extração de texto de PDF, incluindo tratamento de documentos ilegíveis
- Classificação por palavra-chave com tratamento explícito de ambiguidade, em vez de assumir uma resposta única quando o dado não permite certeza
- Estruturas de dados aninhadas (dicionário de listas) para mapear regras de negócio reais
- Manipulação seletiva de arquivos (`os.rename`), incluindo uso de gerenciador de contexto (`with`) para evitar arquivos travados
- Debug orientado a dado real: bugs silenciosos (inconsistência de acentuação entre listas de referência) que só apareceram testando com documentos reais, não em casos ideais
