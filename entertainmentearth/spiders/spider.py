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


class Entertainmentearth(CrawlSpider):
   name = "entertainmentearth"
   allowed_domains = ['entertainmentearth.com']
   start_urls = ['http://entertainmentearth.com']

   ## Initialize the scraper and login
   def __init__(self, *args, **kwargs):
    super(Entertainmentearth, self).__init__(*args, **kwargs)
    self.requests_list=[]
    login_username = '2826259'
    login_password = 'Lee18aH'
    link = 'https://www.entertainmentearth.com/wscheckin.asp?pg=1'
    request = FormRequest(link, formdata={'skip_redirect': '1','custnum': login_username, 'password': login_password, 'x': '14', 'y': '15'}, callback=lambda r:self.set_session(r))
    self.requests_list.append(request)

   def __del__(self):
    print "Stopping"

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
      request = FormRequest(link, formdata={'general_keywords': 'a','newSearchBtn': '1',
       'wishlistSearch': '0','NewProductSearch':'0','InStockSearch': '0',
       'company': '', 'companytext': '', 'theme': '', 'themetext': '', 'collect': '',
       'collecttext': '', 'SkuTextArea': '', 'x': '34', 'y': '14'}, callback=lambda r:self.get_report_page(r),
      ##cookies={'Cookie':'ASPSESSIONIDCARDQDQQ=FOHLCNHBOBLDOBENODMDOFDP; cto_lwid=550c1e41-289a-4dd6 -817b-19e7be828a25; _vwo_uuid_v2=D91ABB1C766A258C136FE6540B545F20B|9ecbd9ae21164f32702cb0d2e9799fa9; rsci_vid=64e7961c-f846-bba4-41c4-32e710461044; __asc=5d438b0d162ac86bb70c965a027; __auc=5d438b0d162ac86bb70c965a027; __utma=240942039.1840836561.1523312934.1523312934.1523312934.1; __utmc=240942039; __utmz=240942039.1523312934.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __qca=P0-1873946411-1523312934125; _ga=GA1.2.1840836561.1523312934; _gid=GA1.2.1108086347.1523312934; __zlcmid=lqhFsQRQWWOiBg; __utmb=240942039.2.10.1523312934; sc_fb_session={%22start%22:1523312934021%2C%22p%22:2}; sc_fb={%22v%22:0.3%2C%22t%22:72%2C%22p%22:2%2C%22s%22:1%2C%22b%22:[]%2C%22pv%22:[]%2C%22tr%22:0%2C%22e%22:[]}; _gat=1; rsci_wait=1'},
       dont_filter=True)
      print request
      yield request

   def set_session(self, response):
    print 'Setting session'
    link = 'https://www.entertainmentearth.com/javascripts/session.asp?code=932471'
    request = Request(link, callback=lambda r:self.get_JSScript1(r), headers={'X-Requested-With': 'XMLHttpRequest'}, dont_filter=True)
    yield request

   def get_JSScript1(self, response):
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
    inspect_response(response, self)
    print 'Iterating over results in report'
    hxs = Selector(response)
    print response.url
    # for page in hxs.xpath('/html/body/table/tr[1]/td//a[@href]'):
    #   print page.extract()
    #   ## yield this page to iterate
    # for item in hxs.xpath('/html/body/table//tr'):
    #   print item.xpath('./td[1]/b/text()').extract()
    #   print item.xpath('./td[2]/text()').extract()


