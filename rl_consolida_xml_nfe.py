import xml.etree.ElementTree as ET
import os

# definir o caminho da pasta
pasta = 'C:/temp/xml_nfe'
prefix = "{http://www.portalfiscal.inf.br/nfe}"
# Abrir o arquivo XML

#tree = ET.parse('C:/temp/xml_nfe/procNfe_Planet_car.xml') 
#root = tree.getroot()
#
# obter uma lista de todos os arquivos na pasta
lista_arquivos = os.listdir(pasta) 

# ler cada arquivo XML e fazer algo com os dados
for arquivo in lista_arquivos:
    if arquivo.endswith('.xml'):
        caminho_arquivo = os.path.join(pasta, arquivo)
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()

    # contar o número de ocorrências da tag "det"
    num_itens = len(root.findall('.//{http://www.portalfiscal.inf.br/nfe}det'))
    qtd_reg = 0
    ler_reg = 0
    n_item = '1'
    lista = []

    while qtd_reg <  num_itens:
        ler_reg = ler_reg + 1
        for info in root.findall(".//{}det[@nItem='{}']//{}xProd".format(prefix, ler_reg, prefix)):
            produto = info.text
        for info in root.findall(".//{}det[@nItem='{}']//{}vProd".format(prefix, ler_reg, prefix)):
            valor = info.text
        qtd_reg =  qtd_reg + 1
        lista.append({'Produto': produto, 'valor': valor}) 

    print (lista)     



# exibir o resultado
print('A NFe contém {} itens.'.format(num_itens))