import requests
from bs4 import BeautifulSoup

# Informe a chave de acesso da nota fiscal que deseja obter o XML
chave_acesso = '35230307583668000158550010000612421560467900'

# URL da página que contém o link para download do XML da NF-e
url = f'https://www.receita.fazenda.gov.br/PessoaJuridica/NFe/ConsultaNFe.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=&nfe={chave_acesso}'

# Faz a requisição HTTP para a página da NF-e
response = requests.get(url, verify=False)

# Faz o parse do conteúdo HTML retornado pela página da NF-e
soup = BeautifulSoup(response.content, 'html.parser')

# Encontra o link para download do XML da NF-e
link_xml = soup.find('a', {'id': 'hyperlinkDownload'})['href']

# Faz o download do XML da NF-e
xml = requests.get(link_xml).content

# Salva o XML em um arquivo
with open(f'{chave_acesso}.xml', 'wb') as f:
    f.write(xml)
