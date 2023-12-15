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

    script = """
    function main(splash, args)
      splash:set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0')
      splash.private_mode_enabled = false
      assert(splash:go(args.url))
      assert(splash:wait(1))
      all_matches = assert(splash:select_all('label.btn.btn-sm.btn-primary'))
      all_matches[2]:mouse_click()
      assert(splash:wait(1))
      splash:set_viewport_full()
      return {
        html = splash:html(),
        png = splash:png()
      }
    end

    """

    def parse(self, response):
        raw = response.body
        print(raw)
        # json_response = json.loads(json.dumps(xmltodict.parse(raw)))
        # print(json_response)
