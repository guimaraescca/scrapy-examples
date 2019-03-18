# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

from scrapy.exceptions import DropItem


class DuplicatesPipeline(object):
    """Drop news items corresponding to the same URL."""
    def __init__(self):
        self.url_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.url_seen:
            raise DropItem(f'Duplicated item found: {item}')
        else:
            self.url_seen.add(item['url'])
            return item


class ParsingPipeline(object):
    """Parse scrapped news items."""
    def process_item(self, item, spider):

        item['date'] = '' if item['date'] is None else re.findall(r'(\d{2}/\d{2}/\d{4})', item['date'].strip())[0]

        return item
