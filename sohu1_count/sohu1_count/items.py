# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Sohu1CountItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    read_num = scrapy.Field()
    comments_num = scrapy.Field()
