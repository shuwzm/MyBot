# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MybotItem(scrapy.Item):
    # define the fields for your item here like:

    name = scrapy.Field()
    currentPrice = scrapy.Field()
    Url = scrapy.Field()
    regularPrice = scrapy.Field()
    Discount = scrapy.Field()
    status = scrapy.Field()
    pass
