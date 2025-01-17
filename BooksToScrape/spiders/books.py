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

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    custom_settings = {
        'FEED_URI': 'books.csv',
        'FEED_FORMAT': 'csv',
    }