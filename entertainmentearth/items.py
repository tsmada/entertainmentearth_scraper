# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Field


class entertainmentearthItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    index = scrapy.Field()
    itemno = scrapy.Field()
    name = scrapy.Field()
    availability = scrapy.Field()
    upc = scrapy.Field()
    suggestedretailprice = scrapy.Field()
    mapp = scrapy.Field()
    casepack = scrapy.Field()
    buythiscasequantity = scrapy.Field()
    totalnopiecesincluded = scrapy.Field()
    priceperpiece = scrapy.Field()
    pricepercase = scrapy.Field()
    buythiscasequantity2 = scrapy.Field()
    totalnopiecesincluded2 = scrapy.Field()
    priceperpiece2 = scrapy.Field()
    pricepercase2 = scrapy.Field()
    imgurl = scrapy.Field()
    company = scrapy.Field()
    theme = scrapy.Field()
    producttype = scrapy.Field()
    agefrom = scrapy.Field()
    ageto = scrapy.Field()
    gender = scrapy.Field()
    pass
