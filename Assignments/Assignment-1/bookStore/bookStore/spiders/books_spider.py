import scrapy


class BooksSpider(scrapy.Spider):
    name = "books_spider"

    def start_requests(self):
        urls = ["http://books.toscrape.com/catalogue/page-1.html"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for article in response.css('section li article'):
            image_url = article.css('img.thumbnail::attr(src)').get()
            title = article.css('h3 a::text').get()
            price = article.css('div.product_price p::text').get()

            yield {
                'image_url': image_url,
                'book_title': title,
                'product_price': price,
            }

            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)