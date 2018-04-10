from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from scrapy.item import Item
from scrapy.http import Request, FormRequest, TextResponse
from entertainmentearth.items import entertainmentearthItem
from scrapy.spiders import CrawlSpider, BaseSpider
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from datetime import datetime
import sys, os, csv, time, uuid, re, string


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
    request = FormRequest(link, formdata={'skip_redirect': '1','custnum': login_username, 'password': login_password, 'x': '14', 'y': '15'}, callback=lambda r:self.request_report(r))
    self.requests_list.append(request)

   def __del__(self):
    print "Deleted"

   def parse(self, response):
    for r in self.requests_list:
        yield r

   def request_report(self, response):
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
       'collecttext': '', 'SkuTextArea': '', 'x': '14', 'y': '15'}, callback=lambda r:self.get_report_page(r),
       headers={
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'en-US,en;q=0.9',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Content-Length': '170',
      'Content-Type': 'application/x-www-form-urlencoded',
      ##'Cookie': 'ASPSESSIONIDCARDQDQQ=BIBGCNHBDLJHIOODINEJJBCE; cto_lwid=b58bb9b6-666f-4b0c-8cc2-627e77141e14; __auc=91c8ea6c162ac326d87b8b242ad; _vwo_uuid_v2=D3981DC6DBE4BC49EA54F96239C8F14B3|5e7157b20d505300d3a939997ed1c75b; rsci_vid=6436ba9d-27fc-af0e-2efe-ce3cd4ea3db4; __utmc=240942039; __utmz=240942039.1523307409.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __qca=P0-2033239022-1523307409551; _ga=GA1.2.716016271.1523307409; _gid=GA1.2.944402124.1523307410; __zlcmid=lqhFrp3532kNtl; _sckey=mb2-5acbd3c61b0af0.57549147; _scsess=sess-2-5acbd3c61b1388.64415921; source%5Faff%5Fv2=GA%2D704038122; source%5Faff=GA%2D704038122; source%5Ftstamp%5Fv2=20180409; source%5Ftstamp=20180409; __asc=9fbc2f48162ad0c3f9c8e72cebf; __utma=240942039.716016271.1523307409.1523312878.1523321686.3; __utmt=1; __utmb=240942039.3.10.1523321686; sc_fb_session={%22start%22:1523307409451%2C%22p%22:12}; sc_fb={%22v%22:0.3%2C%22t%22:641%2C%22p%22:12%2C%22s%22:1%2C%22b%22:[]%2C%22pv%22:[]%2C%22tr%22:0%2C%22e%22:[]}',
      'DNT': '1',
      'Host': 'www.entertainmentearth.com',
      'Origin': 'https://www.entertainmentearth.com',
      'Pragma': 'no-cache',
      'Referer': 'https://www.entertainmentearth.com/wspricelist.asp',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
       }, ##cookies={'Cookie':'ASPSESSIONIDCARDQDQQ=FOHLCNHBOBLDOBENODMDOFDP; cto_lwid=550c1e41-289a-4dd6-817b-19e7be828a25; _vwo_uuid_v2=D91ABB1C766A258C136FE6540B545F20B|9ecbd9ae21164f32702cb0d2e9799fa9; rsci_vid=64e7961c-f846-bba4-41c4-32e710461044; __asc=5d438b0d162ac86bb70c965a027; __auc=5d438b0d162ac86bb70c965a027; __utma=240942039.1840836561.1523312934.1523312934.1523312934.1; __utmc=240942039; __utmz=240942039.1523312934.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __qca=P0-1873946411-1523312934125; _ga=GA1.2.1840836561.1523312934; _gid=GA1.2.1108086347.1523312934; __zlcmid=lqhFsQRQWWOiBg; __utmb=240942039.2.10.1523312934; sc_fb_session={%22start%22:1523312934021%2C%22p%22:2}; sc_fb={%22v%22:0.3%2C%22t%22:72%2C%22p%22:2%2C%22s%22:1%2C%22b%22:[]%2C%22pv%22:[]%2C%22tr%22:0%2C%22e%22:[]}; _gat=1; rsci_wait=1'},
       dont_filter=True)
      print request
      yield request

   def get_report_page(self, response):
    print 'Getting report page'
    link = 'https://www.entertainmentearth.com/excelFriendlyPriceList.asp'
    request = Request(link, callback=lambda r:self.iterate_over_each_page(r), dont_filter=True)
    yield request

   def iterate_over_each_page(self, response):
    print 'Iterating over results in report'
    hxs = Selector(response)
    print response.url
    # for page in hxs.xpath('/html/body/table/tr[1]/td//a[@href]'):
    #   print page.extract()
    #   ## yield this page to iterate
    # for item in hxs.xpath('/html/body/table//tr'):
    #   print item.xpath('./td[1]/b/text()').extract()
    #   print item.xpath('./td[2]/text()').extract()


