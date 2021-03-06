# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class CrawlNewItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    content = scrapy.Field()
    image = scrapy.Field()
    date = scrapy.Field()
    lang = scrapy.Field()
    slug = scrapy.Field()
    url = scrapy.Field()

