from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "fxbook"
    start_urls = [
        "https://www.myfxbook.com/systems/",
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)