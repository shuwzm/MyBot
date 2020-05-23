from MyBot.items import *
import scrapy
from scrapy.spiders import CrawlSpider
from urllib.parse import urljoin
import re


class bestbuySpider(CrawlSpider):
    name = 'bestbuy'
    item = MybotItem()
    allow_domain = 'www.bestbuy.com'
    base_url = 'https://www.bestbuy.com'
    start_urls = ['https://www.bestbuy.com/site/searchpage.jsp?st=surface&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071'
                  '&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys']

    def parse(self, response):
        print('this is the first page %s', response.url)
        numPattern = r'\d+(,)?\d+(\.\d*)?'

        raw_items = response.xpath('//*[@class="sku-item"]')
        for ri in raw_items:
            print(str(ri))
            productName = ri.xpath('.//*[@class="sku-header"]/a/text()').get()
            print(productName)
            currentPrice = ri.xpath('.//*[@class="priceView-hero-price priceView-customer-price"]/span[1]/text()').get()
            m = re.search(numPattern, currentPrice)
            currentPrice = m.group(0)
            currentPrice = currentPrice.replace(',', '')

            savePrice = ri.xpath('.//*[@class="pricing-price__savings"]/text()').get()
            regularPrice = ri.xpath('.//*[@class="pricing-price__regular-price sr-only"]/text()').get()
            url = urljoin(self.base_url, ri.xpath('.//*[@class="image-link"]/@href').get())
            status = ri.xpath('.//button[contains(@class,"add-to-cart-button")]/text()').get()
            imageUrl = ri.xpath('.//*[@class="product-image"]/@src').get()
            if savePrice is None:
                savePrice = 0
            else:
                m = re.search(numPattern, savePrice)
                savePrice = m.group(0)
                savePrice = savePrice.replace(',', '')

            if regularPrice is None:
                regularPrice = currentPrice
            else:
                m = re.search(numPattern, regularPrice)
                regularPrice = m.group(0)
                print('regularPrice:', regularPrice)
                regularPrice = regularPrice.replace(',', '')
            print('\n')
            regularPrice = float(regularPrice)
            savePrice = float(savePrice)
            currentPrice = float(currentPrice)
            yield {
                'productName': productName,
                'url': url,
                'imageUrl': imageUrl,
                'currentPrice': currentPrice,
                'regularPrice': regularPrice,
                'discount': "{:.0%}".format(savePrice / regularPrice),
                'status': status,
            }
        # item['productName'] = productName
        # item['url'] = url
        # item['imageUrl'] = imageUrl
        # item['regularPrice'] = regularPrice
        # item['discount'] = 'test'
        # item['status'] = 'Add to cart'

        # next_page_url = response.xpath(
        #     '//*[@class="sku-list-page-next"]/@href').extract_first()
        # if next_page_url:
        #     yield scrapy.Request(next_page_url, callback=self.parse)
        pass
