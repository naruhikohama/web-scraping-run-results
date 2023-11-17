import scrapy
import json

links_resultados = json.load(open("data_scraped/links_resultados.json"))

print(links_resultados)

class AtivoSpider(scrapy.Spider):
    name = "ativo"
    allowed_domains = ["www.ativo.com", "webservices.esferabr.com.br"]
    start_urls = links_resultados

    def parse(self, response):
        json_response = json.loads(response.body)

        print(len(json_response))

        for item in json_response:
            nome = item.get('nome')
            num_peito = item.get('num_peito')
            nome_evento = item.get('nome_evento')
            sexo = item.get('sexo')
            modalidade = item.get('modalidade')
            categoria = item.get('categoria')
            tempo_total = item.get('tempo_total')
            tempo_bruto = item.get('tempo_bruto')
            pace = item.get('pace')
            classificacao_categoria = item.get('itens').get('classificacao_categoria')
            classificacao_sexo = item.get('itens').get('classificacao_sexo')
            classificacao_total = item.get('itens').get('classificacao_total')
            mais_rapido_que = item.get('mais_rapido_que')

            yield {
                'nome': nome.upper(),
                'num_peito': num_peito,
                'nome_evento': nome_evento,
                'sexo': sexo,
                'modalidade': modalidade,
                'categoria': categoria,
                'tempo_total': tempo_total,
                'tempo_bruto': tempo_bruto,
                'pace': pace,
                'classificacao_categoria': classificacao_categoria,
                'classificacao_sexo': classificacao_sexo,
                'classificacao_total': classificacao_total,
                'mais_rapido_que': mais_rapido_que
            }

        if len(json_response) == 10:
            next_page = response.urljoin(f"{response.url.rsplit('=', 1)[0]}={int(response.url.split('=')[-1]) + 10}")
            yield scrapy.Request(next_page, callback=self.parse)



