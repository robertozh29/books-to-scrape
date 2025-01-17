import scrapy
import random
import os


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    """
    csv_file_path = 'csv_files/quotes.csv'
    def __init__(self):
        super(QuotesSpider, self).__init__()
        if os.path.exists(self.csv_file_path):
            os.remove(self.csv_file_path)
    """

    def parse(self, response):
        tags = response.css("span.tag-item a.tag::text").getall()
        random_tag = tags[random.randint(0,len(tags))]
        for quote in response.css("div.quote"):
            yield {
                "Etiqueta": random_tag,
                "Cita": quote.css("span.text::text").get(),
                "Autor": quote.css("span small.author::text").get(),
            }

    custom_settings = {
        'FEED_URI': 'csv_files/quotes.csv',
        'FEED_FORMAT': 'csv',
    }