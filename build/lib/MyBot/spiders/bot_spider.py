import scrapy
from MyBot.items import *
from selenium import webdriver
import logging

import os

class BotSpider(scrapy.Spider):
    name = "bot"
    allowed_domains = ["www.bestbuy.com"]
    
    #start_urls = ["https://www.bestbuy.com/site/apple-ipad-latest-model-with-wi-fi-32gb-space-gray/5985609.p?skuId=5985609"]
    start_urls = ['https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255']

    def __init__(self, *args, **kwargs):
        self.driver = webdriver.Chrome('c:\\webdriver\chromedriver.exe')
    
    #def start_requests(self):
     #   self.driver.get(response.url)


    def parse(self, response):
        #item = RedwineItem() 
        #print(response.text)
        #price = response.xpath('//div[@class="price-box pricing-lib-price-8-2013-8"]/div/div/div/span[1]/text()').extract_first()
        #name = response.xpath('//div[@class="item ellipsis"]/text()').extract_first()
        self.driver.get(response.url)
        price = self.driver.find_element_by_xpath('//div[@class="price-box pricing-lib-price-8-2013-8"]/div/div/div/span[1]').text

        atc = self.driver.find_element_by_xpath('//*[@class="fulfillment-add-to-cart-button"]/div/button').text

        print("price is " + str(price))
        print(atc)

        logging.warning('The price is'+str(price))
        logging.warning('status:'+atc)

        

