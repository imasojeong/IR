from pathlib import Path

import scrapy


class MovieSpider(scrapy.Spider):
    name = "movie"

    def start_requests(self):
        urls = [
            "https://www.netflix.com/browse/genre/34399",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")