import datetime

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from MyBot.items import *
# from pyvirtualdisplay import Display
import time
from selenium.webdriver.firefox.options import Options


class BotSpider(scrapy.Spider):
    name = "bot"
    allowed_domains = ["www.bestbuy.com"]

    # start_urls = ["https://www.bestbuy.com/site/apple-ipad-latest-model-with-wi-fi-32gb-space-gray/5985609.p?skuId
    # =5985609"]
    start_urls = [
        'https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255',
        'https://www.bestbuy.com/site/nintendo-switch-32gb-console-gray-joy-con/6364253.p?skuId=6364253'
        # 'https://www.bestbuy.com/site/apple-ipad-latest-model-with-wi-fi-32gb-space-gray/5985609.p?skuId=5985609'
    ]

    def __init__(self, *args, **kwargs):
        # Try to run on background and speed up, but not work.
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--no-proxy-server')
        # chrome_options.add_argument("--proxy-server='direct://'")

        # chrome_options.add_argument("--proxy-bypass-list=*")
        # self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='c:\\webdriver\chromedriver.exe')

        # Cannot use in Windows, because pyvirtualDisplay need xvfb
        # display = Display(visible=0, size=(800,600))
        # display.start()

        # self.driver = webdriver.Chrome('c:\\webdriver\chromedriver.exe')

        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=options, executable_path='c:\\webdriver\geckodriver.exe')

    # def start_requests(self):
    #   self.driver.get(response.url)

    def parse(self, response):
        item = MybotItem()
        self.driver.get(response.url)

        name = self.driver.find_element_by_xpath('//*[@class="sku-title"]').text
        currentPrice = self.driver.find_element_by_xpath(
            '//div[@class="price-box pricing-lib-price-8-2013-8"]/div/div/div/span[1]').text

        isPresent = len(self.driver.find_elements_by_class_name('pricing-price__regular-price'))
        regularPrice = currentPrice

        if isPresent > 0:
            regularPrice = self.driver.find_element_by_xpath('//*[@class="pricing-price__regular-price"]').text


        status = self.driver.find_element_by_xpath('//*[@class="fulfillment-add-to-cart-button"]/div/button').text

        print("currentPrice is " + str(currentPrice))
        print("name is " + str(name))
        print("regularPrice is " + str(regularPrice))
        print(status)

        product = ''
        if 'Nintendo' in name and 'Red' in name:
            product = 'SwitchRed'
        elif 'Nintendo' in name and 'Gray' in name:
            product = 'SwitchGray'
        elif 'iPad' in name:
            product = 'iPad'
        else:
            product = 'abc'

        to_day = datetime.datetime.now()
        dataFile = "data/scrapy {} {} {} {}.data".format(product, to_day.year, to_day.month, to_day.day)

        try:
            file = open(dataFile, 'a+')
            # file.write('Name is: %s \n', name)
            # file.write('The price is %s \n', str(price))
            # file.write('status: %s \n', atc)
            # file.close()
            file.write('Name is: ' + name + '\n')
            file.write('The price is ' + str(currentPrice) + '\n')
            file.write('status: ' + status + '\n')
            file.close()
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))

        item['name'] = name
        item['currentPrice'] = currentPrice
        item['regularPrice'] = regularPrice
        item['status'] = status

        yield item
