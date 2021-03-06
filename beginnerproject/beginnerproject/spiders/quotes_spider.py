import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/tag/inspirational/page/1/',
            "https://quotes.toscrape.com/tag/inspirational/page/2/"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_id = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page_id

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

