import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    current_page = 1
    max_page = 2

    custom_settings = {
        'DOWNLOAD_DELAY': 1,
    }

    def parse(self, response):

        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small::text').get(),
            }


        if self.current_page < self.max_page:
            next_page = response.css('li.next a::attr(href)').get()
            if next_page:
                self.current_page += 1
                yield response.follow(next_page, callback=self.parse)