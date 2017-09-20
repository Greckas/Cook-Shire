import scrapy
import urlparse

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector



class CookspiderSpider(CrawlSpider):
    name = "Cookspider"
    allowed_domains = ["cook.qld.gov.au"]
    start_urls = [
        "http://www.cook.qld.gov.au/"
  
    ]

    rules = (
       Rule(LinkExtractor(allow=r'/', deny=(), unique=True),
           callback='parse_item', follow=True),
    )

    def parse_item(self, response):
       i = {}
       #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
       #i['name'] = response.xpath('//div[@id="name"]').extract()
       #i['description'] = response.xpath('//div[@id="description"]').extract()
       i['url'] = response.url
       sel = response.xpath("//div[@class='portlet-body']")
       i['title'] = ''.join(response.xpath('/html/head/title/text()').extract()).strip()
       i['text'] = ''.join(sel.xpath("//div[@class='portlet-content']").extract()).strip()
       # i['file_urls'] = []
       # base_url = response.url
       # for a in response.xpath('//a[@href]/@href'):
       #      link = a.extract()
       #      if link.endswith('.pdf'):
       #        i['file_urls'] = (urlparse.urljoin(base_url, link))
       return i
