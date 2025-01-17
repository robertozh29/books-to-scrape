import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for book in response.css("article.product_pod"):
            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "Price": book.css("div.product_price p.price_color::text").get(),
                "Availability": "".join(book.css("div.product_price p.availability::text").get()).strip()
            }