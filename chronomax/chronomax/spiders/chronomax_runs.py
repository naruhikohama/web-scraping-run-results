import scrapy


class ChronomaxRunsSpider(scrapy.Spider):
    name = "chronomax_runs"
    allowed_domains = ["www.chronomax.com.br"]
    start_urls = ["https://www.chronomax.com.br/index.php/Resultado"]

    def parse(self, response):
        pass
