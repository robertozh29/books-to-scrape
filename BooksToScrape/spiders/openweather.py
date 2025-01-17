import scrapy
import json
import private_keys

class OpenweatherSpider(scrapy.Spider):
    name = "weather"
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "5d2e48b59c0f16c0631281023411b831"
    cities = ["London", "Washington","New York", "Tokyo"]

    def start_requests(self):
        for city in self.cities:
            url = f"{self.api_url}?q={city}&appid={private_keys.API_KEY}"
            yield scrapy.Request(url, callback=self.parse, meta={'city': city})

    def parse(self, response):
        data = json.loads(response.text)

        city = response.meta['city']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_condition = data['weather'][0]['description']

        yield {
            'Ciudad': city,
            'Temperatura': temperature,
            'Humedad': humidity,
            'Condiciones climaticas': weather_condition
        }

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'csv_files/weather.csv',
    }