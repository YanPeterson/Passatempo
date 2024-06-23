import requests
from PIL import Image
import urllib.request as ur
from bs4 import BeautifulSoup
import pandas as pd

url = "https://lista.mercadolivre.com.br/geladeira#D[A:geladeira]"
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

produtos_tabela = {"nome_do_produto":[],
                   "preco":[],
                   "imagem":[],
                   "tag":[] }
def getdata(url):
    x = 1
    site = requests.get(url, headers=header)
    soup = BeautifulSoup(site.content, "html.parser")
    produtos = soup.findAll("div", class_="ui-search-result__wrapper")

    for produto in produtos:
        nome_do_produto = produto.find("h2", class_="ui-search-item__title").get_text()
        preco = produto.find("span", class_="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript").get_text()
        imagem = produto.find("img", class_="ui-search-result-image__element lazy-loadable")['data-src']
        tag = produto.find("img", class_="ui-search-result-image__element lazy-loadable")['alt']

        # Baixar todas as imagens caso necessário

        """while produto in produtos:
            ur.urlretrieve(imagem, f"imagens\imagem{x}.wepb") 
            x = x + + 1
            break"""

        produtos_tabela['nome_do_produto'].append(nome_do_produto)
        produtos_tabela['preco'].append(preco)
        produtos_tabela['imagem'].append(imagem)
        produtos_tabela['tag'].append(tag)

getdata("https://lista.mercadolivre.com.br/ventilador#D[1:ventilador]")
getdata("https://lista.mercadolivre.com.br/cadeira#D[1:cadeira]")

df = pd.DataFrame(produtos_tabela)

df.to_csv("lista.csv", encoding="utf-8", index=False)


