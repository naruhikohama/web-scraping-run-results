import scrapy
import pandas as pd
import xml.etree.ElementTree as ET
import xmltodict
import json

chronomax = pd.read_csv('data_scraped/chronomax_runs_tratado.csv')

links = chronomax['link'].tolist()
print(links[0])

class ChronomaxResultadosSpider(scrapy.Spider):
    name = "chronomax_resultados"
    allowed_domains = ["www.chronomax.com.br"]
    start_urls = [links[0]]

    def parse(self, response):
        rows = response.xpath("//body")
        print(rows)
