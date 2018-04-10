from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from scrapy.item import Item
from scrapy.http import Request, FormRequest, TextResponse
from entertainmentearth.items import entertainmentearthItem
from scrapy.spiders import CrawlSpider, BaseSpider
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from datetime import datetime
import sys, os, csv, time, uuid, re, string
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser
from random import randint
import time


class Entertainmentearth(CrawlSpider):
   name = "entertainmentearth"
   allowed_domains = ['entertainmentearth.com']
   start_urls = ['http://entertainmentearth.com']

   ## Initialize the scraper and login
   def __init__(self, *args, **kwargs):
    super(Entertainmentearth, self).__init__(*args, **kwargs)
    self.requests_list=[]
    self.page = 0
    login_username = '2826259'
    login_password = 'Lee18aH'
    link = 'https://www.entertainmentearth.com/wscheckin.asp?pg=1'
    request = FormRequest(link, formdata={'skip_redirect': '1','custnum': login_username, 'password': login_password, 'x': '14', 'y': '15'}, callback=lambda r:self.set_session(r))
    self.requests_list.append(request)

   def __del__(self):
    print "Stopping"


    ## function to generate a random number for sr.js
   def generate_serial(self, n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

   def parse(self, response):
    for r in self.requests_list:
        yield r

   def request_report(self, response):
      print response.headers
      link = 'https://www.entertainmentearth.com/wspricelist.asp?pg=1'
      # general_keywords: a
      # newSearchBtn: 1
      # wishlistSearch: 0
      # NewProductSearch: 0
      # InStockSearch: 0
      # company: 
      # companytext: 
      # theme: 
      # themetext: 
      # collect: 
      # collecttext: 
      # SkuTextArea: 
      # x: 51
      # y: 16
      request = FormRequest(link, formdata={'general_keywords': 'marvel','newSearchBtn': '1',
       'wishlistSearch': '0','NewProductSearch':'0','InStockSearch': '0',
       'company': '', 'companytext': '', 'theme': '', 'themetext': '', 'collect': '',
       'collecttext': '', 'SkuTextArea': '', 'x': '34', 'y': '14'}, callback=lambda r:self.get_report_page(r),
      ##cookies={'Cookie':'ASPSESSIONIDCARDQDQQ=FOHLCNHBOBLDOBENODMDOFDP; cto_lwid=550c1e41-289a-4dd6 -817b-19e7be828a25; _vwo_uuid_v2=D91ABB1C766A258C136FE6540B545F20B|9ecbd9ae21164f32702cb0d2e9799fa9; rsci_vid=64e7961c-f846-bba4-41c4-32e710461044; __asc=5d438b0d162ac86bb70c965a027; __auc=5d438b0d162ac86bb70c965a027; __utma=240942039.1840836561.1523312934.1523312934.1523312934.1; __utmc=240942039; __utmz=240942039.1523312934.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __qca=P0-1873946411-1523312934125; _ga=GA1.2.1840836561.1523312934; _gid=GA1.2.1108086347.1523312934; __zlcmid=lqhFsQRQWWOiBg; __utmb=240942039.2.10.1523312934; sc_fb_session={%22start%22:1523312934021%2C%22p%22:2}; sc_fb={%22v%22:0.3%2C%22t%22:72%2C%22p%22:2%2C%22s%22:1%2C%22b%22:[]%2C%22pv%22:[]%2C%22tr%22:0%2C%22e%22:[]}; _gat=1; rsci_wait=1'},
       dont_filter=True)
      yield request

   def set_session(self, response):
    print 'Setting Session'
    link = 'https://www.entertainmentearth.com/javascripts/session.asp?code=' + str(self.generate_serial(6))
    request = Request(link, callback=lambda r:self.get_JSScript1(r), headers={'X-Requested-With': 'XMLHttpRequest'}, dont_filter=True)
    yield request

   def get_JSScript1(self, response):
    print response.headers
    link = 'https://www.entertainmentearth.com/javascripts/JScript1.js'
    request = Request(link, callback=lambda r:self.get_popup(r), dont_filter=True)
    yield request

   def get_popup(self, response):
    link = 'https://www.entertainmentearth.com/dynpopdesc4.js'
    request = Request(link, callback=lambda r:self.get_hdupdate(r), dont_filter=True)
    yield request

   def get_hdupdate(self, response):
    link = 'https://www.entertainmentearth.com/javascripts/hdupdate.js'
    request = Request(link, callback=lambda r:self.get_sr(r), dont_filter=True)
    yield request

   def get_sr(self, response):
    link = 'https://www.entertainmentearth.com/javascripts/sr.js'
    request = Request(link, callback=lambda r:self.request_report(r), dont_filter=True)
    yield request

   def get_report_page(self, response):
    print response.headers
    print 'Getting report page'
    link = 'https://www.entertainmentearth.com/excelFriendlyPriceList.asp'
    request = Request(link, callback=lambda r:self.iterate_over_each_page(r), dont_filter=True)
    yield request

   def iterate_over_each_page(self, response):
    item = entertainmentearthItem()
    print 'Iterating over results in report'
    hxs = Selector(response)
    if self.page == 0:
      for page in hxs.xpath('/html/body/table/tr[1]/td//a/@href'):
        link = 'https://www.entertainmentearth.com/' + page.extract()
        request = Request(link, callback=lambda r:self.iterate_over_each_page(r), dont_filter=True)
        yield request
      self.page = 1
      ## yield this page to iterate
    for row in hxs.xpath('/html/body/table//tr')[1:-1]:
      item['itemno'] = row.xpath('./td[2]/text()').extract()
      item['name'] = row.xpath('./td[3]/text()').extract()
      item['availability'] = row.xpath('./td[4]/text()').extract()
      item['upc'] = row.xpath('./td[5]/text()').extract()
      item['suggestedretailprice'] = row.xpath('./td[6]/text()').extract()
      item['mapp'] = row.xpath('./td[7]/text()').extract()
      item['casepack'] = row.xpath('./td[8]/text()').extract()
      item['buythiscasequantity'] = row.xpath('./td[9]/text()').extract()
      item['totalnopiecesincluded'] = row.xpath('./td[10]/text()').extract()
      item['priceperpiece'] = row.xpath('./td[11]/text()').extract()
      item['pricepercase'] = row.xpath('./td[12]/text()').extract()
      item['buythiscasequantity2'] = row.xpath('./td[13]/text()').extract()
      item['totalnopiecesincluded2'] = row.xpath('./td[14]/text()').extract()
      item['priceperpiece2'] = row.xpath('./td[15]/text()').extract()
      item['pricepercase2'] = row.xpath('./td[16]/text()').extract()
      item['imgurl'] = row.xpath('./td[17]/a/img[@src]').extract()
      item['company'] = row.xpath('./td[18]/text()').extract()
      item['theme'] = row.xpath('./td[19]/text()').extract()
      item['producttype'] = row.xpath('./td[20]/text()').extract()
      item['agefrom'] = row.xpath('./td[21]/text()').extract()
      item['ageto'] = row.xpath('./td[22]/text()').extract()
      item['gender'] = row.xpath('./td[23]/text()').extract()
      yield item


