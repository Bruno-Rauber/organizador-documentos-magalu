import os

pasta = "C:/Users/bruno/Desktop/MAGALU 5240 69  5235 98"

arquivos = os.listdir(pasta)

pdf = [arquivo for arquivo in arquivos if arquivo.endswith(".pdf")] # lista itera arquivos e se termina com .pdf salva

print(pdf)