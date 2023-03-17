import os

# Define o caminho da pasta
caminho_pasta = r'C:\temp\xml_nfe\procNfe_Planet_car.xml'

# Lista todos os arquivos na pasta
arquivos = os.listdir(caminho_pasta)

# Exibe a extensão de cada arquivo
for arquivo in arquivos:
    # Usa o método splitext() para dividir o nome do arquivo e a extensão
    nome_arquivo, extensao = os.path.splitext(arquivo)
    print(f"A extensão do arquivo {arquivo} é '{extensao}'")
