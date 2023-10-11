import scrapy

class MlSpider(scrapy.Spider):
    name = "ML"
    start_urls = ["https://matheusdosreislp.netlify.app/"]

    def parse(self, response, **kwargs):
        for i in response.xpath('//div[@class="card"]'):
            title = i.xpath('.//div[@class="body-desc"]//p//text()').get()
            link = i.xpath('.//div[@class="body-btn"]//a/@href').get()

            yield {
                'title': title,
                'link': link,
            }
