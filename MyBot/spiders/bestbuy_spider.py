from MyBot.items import MybotItem
import scrapy
from scrapy.spiders import CrawlSpider

class bestbuySpider(CrawlSpider):
    name = 'bestbuy'
    item = MybotItem()
    allow_domain = 'www.bestbuy.com'
    start_urls = ['https://www.bestbuy.com/site/searchpage.jsp?st=ps4&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071'
                  '&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys']


    def parse(self, response):
        print('this is the first page %s', response.url)

        raw_items = response.xpath('//*[@class="sku-item"]')
        for ri in raw_items:
            print(str(ri))
            producteName = ri.xpath('.//*[@class="sku-header"]/a/text()').get()
            print(producteName)
            currentPrice = ri.xpath('.//*[@class="priceView-hero-price priceView-customer-price"]/span[1]/text()').get()
            savePrice = ri.xpath('.//*[@class="pricing-price__savings"]/text()').get()
            regularPrice = ri.xpath('.//*[@class="pricing-price__regular-price sr-only"]/text()').get()
            if savePrice == None :
                savePrice = 0
            if regularPrice == None:
                regularPrice = currentPrice
            print("Current: %s %s %s", currentPrice, savePrice, regularPrice)
            print('\n')

       # next_page_url = response.xpath(
       #     '//*[@class="sku-list-page-next"]/@href').extract_first()
       # if next_page_url:
       #     yield scrapy.Request(next_page_url, callback=self.parse)
        pass
