import scrapy
import json

class EventosSpider(scrapy.Spider):
    name = "eventos"
    allowed_domains = ["www.ativo.com"]
    start_urls = ["https://www.ativo.com/eventos.json"]

    def parse(self, response):
        json_response = json.loads(response.body)
        # print(len(json_response))

        for item in json_response:
            id_evento = item.get('id_evento')
            nome = item.get('post_title')
            data = item.get('dt_evento')
            cidade = item.get('ds_cidade')
            estado = item.get('ds_estado')
            tipo_evento = item.get('ds_tipo_evento')
            evento_terceiro = item.get('evento_de_terceiro')
            organizador = item.get('nome_organizador')
            id_organizador = item.get('id_organizador')
        
            yield {
                'id_evento': id_evento,
                'nome': nome,
                'data': data,
                'cidade': cidade,
                'estado': estado,
                'tipo_evento': tipo_evento,
                'evento_terceiro': evento_terceiro,
                'organizador': organizador,
                'id_organizador': id_organizador
            }
