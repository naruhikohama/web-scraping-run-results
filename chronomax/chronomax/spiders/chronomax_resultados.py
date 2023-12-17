import scrapy
import pandas as pd
from scrapy_splash import SplashRequest
from scrapy.selector import Selector

chronomax = pd.read_csv('data_scraped/chronomax_runs_tratado.csv')

links = chronomax['link'].tolist()
print(links[0])

class ChronomaxResultadosSpider(scrapy.Spider):
    name = "chronomax_resultados"
    allowed_domains = ["www.chronomax.com.br"]
    # start_urls = [links[0]]

    script = """
        function main(splash, args)
        splash:set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0')
        splash.private_mode_enabled = false
        assert(splash:go(args.url))
        assert(splash:wait(3))
        splash:set_viewport_full()
        
        return {
            html = splash:html(),
            png = splash:png()
        }
        end
    """

    def start_requests(self):
        yield SplashRequest(
            url=links[0],
            callback=self.parse,
            endpoint="execute",
            args={
                "lua_source": self.script
            }
        )

    def parse(self, response):
        raw = response.body
        print(type(raw))
        rows = Selector(body = raw, encoding="utf8").xpath('//table[@id="tabres"]//tr')
        print(rows)

        for row in rows:
            posicao = row.xpath("./td[1]/text()").get()
            # nome = Selector(body=row, encoding = 'utf8').xpath("./td[3]/text()").get()
            # posicao = row.selector.xpath("./td[1]/text()").get()
            # num_peito = row.selector.xpath("./td[2]/text()").get()
            nome = row.selector.xpath("./td[3]/text()").get()
            # equipe = row.selector.xpath("./td[4]/text()").get()
            # sexo = row.selector.xpath("./td[5]/text()").get()
            # categoria = row.selector.xpath("./td[6]/text()").get()
            # pos_categoria = row.selector.xpath("./td[7]/text()").get()
            # parcial_1 = row.selector.xpath("./td[8]/text()").get()
            # parcial_2 = row.selector.xpath("./td[9]/text()").get()
            # tempo_liquido = row.selector.xpath("./td[10]/text()").get()
            # tempo_bruto = row.selector.xpath("./td[11]/text()").get()
            # pace_medio = row.selector.xpath("./td[12]/text()").get()

            yield {
                # 'posicao': posicao,
                # 'num_peito': num_peito,
                # 'nome': nome,
                # 'equipe': equipe,
                # 'sexo': sexo,
                # 'categoria': categoria,
                # 'pos_categoria': pos_categoria,
                # 'parcial_1': parcial_1,
                # 'parcial_2': parcial_2,
                # 'tempo_liquido': tempo_liquido,
                # 'tempo_bruto': tempo_bruto,
                # 'pace_medio': pace_medio
            }
