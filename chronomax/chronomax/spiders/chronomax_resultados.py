import scrapy
import pandas as pd
import xmltodict
import json

chronomax = pd.read_csv('data_scraped/chronomax_runs_tratado.csv')

links = chronomax['link'].tolist()
print(links[0])

class ChronomaxResultadosSpider(scrapy.Spider):
    name = "chronomax_resultados"
    allowed_domains = ["www.chronomax.com.br"]
    start_urls = ['https://www.chronomax.com.br/resultados/2023/2592/meia_maratona_do_contorno.clax?t=1702436698104']

    def parse(self, response):
        raw = response.body
        print(raw)
        # json_response = json.loads(json.dumps(xmltodict.parse(raw)))
        # print(json_response)
