📄 Projeto: Organizador de Documentos de Cadastro (Bloco 1)

Descrição
Script que lê uma pasta com os PDFs de um cliente, identifica automaticamente o tipo de cada documento e o nome do cliente (quando o PDF tem texto legível), renomeia e organiza os arquivos em pastas, e confere se a documentação obrigatória para aquele tipo de cadastro (Transferência PF/PJ ou Concessão) está completa — sinalizando o que falta ou o que não conseguiu ler.

Valor pro portfólio/vaga
Conta a história de um projeto nascido de um problema real de trabalho, não de exercício de curso. Demonstra leitura/manipulação de arquivos, tratamento de dados incompletos ou inesperados (foto vs PDF) sem quebrar o programa, e lógica de negócio real (regras diferentes por tipo de cadastro) — exatamente o tipo de coisa que uma vaga Junior de automação valoriza: saber lidar com o "mundo real bagunçado", não só o caso ideal.

Tecnologias

pdfplumber (leitura de texto de PDF)
os / pathlib (manipulação de arquivos e pastas)
dicionários (mapear tipo de cadastro → documentos obrigatórios)

Pré-requisitos
Tudo já coberto pelo Módulo 6 (Basics Extended): strings, listas, dicionários, funções. Não depende de módulos futuros.

O que vai aprender

Ler conteúdo de arquivos PDF por código
Buscar padrões de texto (keyword matching) pra classificar informação
Organizar lógica de negócio real em estrutura de dados (dicionários aninhados)
Tratar exceção/caso que o programa não sabe resolver, sem quebrar (foto sem texto)
Renomear e mover arquivos programaticamente

Etapas (cada uma vira um ciclo de prática, com exercício antes da solução)

Ler uma pasta e listar os PDFs dentro dela
Abrir um PDF e extrair o texto com pdfplumber
Detectar se o PDF tem texto legível ou é imagem/foto (e sinalizar quando não conseguir ler)
Criar o "de-para" de documentos obrigatórios por tipo de cadastro (dicionário)
Buscar palavras-chave no texto pra identificar o tipo de documento
Extrair o nome do cliente do texto (quando disponível, ex: CNH)
Renomear e mover o arquivo pra pasta organizada
Rodar a conferência final: o que está completo, o que falta, o que precisa de checagem manual