import fitz

# Abre o arquivo PDF em modo de leitura binária
with fitz.open('C:/temp/nota_pdf/NOTA FISCAL 21789 GALASSI.pdf') as pdf_file:
    # Obtém o número de páginas do arquivo
    num_pages = pdf_file.page_count

    # Lê cada página do arquivo
    for page_num in range(num_pages):
        # Obtém a página atual
        page = pdf_file.load_page(page_num)

        # Extrai o texto da página
        text = page.get_text()

        # Imprime o texto da página
        print(text)