# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from hearthstone_database.items import HearthstoneDatabaseItem


class HearthpwnListingSpider(scrapy.Spider):
    name = 'hearthpwn_listing'
    allowed_domains = ['hearthpwn.com']
    start_urls = ['https://www.hearthpwn.com/cards?display=1&filter-premium=1']

    def parse(self, response):
        table_rows = response.xpath("//table[@id='cards']/tbody/tr")

        for row in table_rows:
            loader = ItemLoader(item=HearthstoneDatabaseItem(), selector=row)
            loader.add_xpath('name', "td[@class='col-name']/a/text()")
            loader.add_xpath('type', "td[@class='col-type']/text()")
            loader.add_xpath('card_class', "td[@class='col-class']/text()")
            loader.add_xpath('cost', "td[@class='col-cost']/text()")
            loader.add_xpath('attack', "td[@class='col-attack']/text()")
            loader.add_xpath('health', "td[@class='col-health']/text()")
            yield loader.load_item()
