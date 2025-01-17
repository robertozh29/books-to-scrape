import scrapy
import mykeys
import json

class OpenweatherSpider(scrapy.Spider):
    name = "weather"
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "5d2e48b59c0f16c0631281023411b831"
    cities = ["London", "Washington"]

    def start_request(self):
        for city in self.cities:
            url = f"{self.api_url}?q={city}&appid={self.api_key}"
            yield scrapy.Request(url, callback=self.parse, meta={'city': city})

    def parse(self, response):
        self.log(f"----------------Parsing response for {response.url}")
        print(f"--------------------------Parsing response for {response.url}")
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
        'FEED_URI': 'weather.csv',
    }