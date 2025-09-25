import PyPDF2
from PyPDF2.errors import PdfReadError

def ler_pdf(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as arquivo_pdf:
            pdf = PyPDF2.PdfReader(arquivo_pdf)
            texto_primeira_pagina = pdf.pages[0].extract_text()
            return texto_primeira_pagina
        
    except FileExistsError:
        print("Arquivo não encontrado")
        return None
    except PdfReadError:
        print("Erro ao ler o arquivo PDF")
        return None

caminho = input("Digite o caminho do arquivo: ").strip('"')
conteudo = ler_pdf(caminho)

if conteudo:
    print("Conteúdo da primeira página: ")
    print(conteudo)
