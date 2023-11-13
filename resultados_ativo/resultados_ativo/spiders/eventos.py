import scrapy


class EventosSpider(scrapy.Spider):
    name = "eventos"
    allowed_domains = ["www.ativo.com"]
    start_urls = ["https://www.ativo.com/calendario/eventos/"]

    def parse(self, response):
        pass
