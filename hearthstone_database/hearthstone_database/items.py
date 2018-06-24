# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HearthstoneDatabaseItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    card_class = scrapy.Field()
    cost = scrapy.Field()
    attack = scrapy.Field()
    health = scrapy.Field()
