# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MybotItem(scrapy.Item):
    # define the fields for your item here like:

    productName = scrapy.Field()
    currentPrice = scrapy.Field()
    url = scrapy.Field()
    imageUrl = scrapy.Field()
    regularPrice = scrapy.Field()
    discount = scrapy.Field()
    status = scrapy.Field()
    pass
