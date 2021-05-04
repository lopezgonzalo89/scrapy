import scrapy

# scrapy crawl mercadoads -O test.json


class QuotesSpider(scrapy.Spider):
    name = "mercadoads"

    """ start_urls = [
        'https://mercadoads.com'
    ] """
    
    def start_requests(self):
        urls = [
            'https://mercadoads.com/change-language'
        ]
        data = {
            'locale': 'pt',
            '_token': 'd2sJmQJXQzs5BgQV6aW0g2yAori1IDoFENgVDVqL',
        }
        for url in urls:
            yield scrapy.http.JsonRequest(
                url=url,
                callback=self.parse,
                method='POST',
                data=data
            )

    def parse(self, response):
        print('')
        print('')
        print('')
        print('PRINTTT: ', response)
        print('')
        print('')
        print('')
        """ for img_icon in response.css('img::attr(data-src)'):
            yield {
                'img-icon': img_icon.get()
            } """
        """ for img in response.css('img::attr(src)'):
            yield {
                'img': img.get()
            } """
        for link in response.css('a::attr(href)'):
            yield {
                'link': link.get()
            }
        for picture in response.css('source::attr(srcset)'):
            yield {
                'picture': picture.get()
            }
        for text in response.css('h1::text'):
            yield {
                'text': text.get()
            }
        """ for video in response.css('source::attr(data-src)'):
            yield {
                'video': video.get()
            } """
        for href in response.css('a::attr(href)'):
            yield response.follow(href, callback=self.parse)
