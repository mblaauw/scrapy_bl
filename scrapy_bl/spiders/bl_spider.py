__author__ = 'MICH'
import re
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy_bl.items import ScrapyBlItem


class BlSpider(BaseSpider):
    name = "bl"
    allowed_domains = ["boekenliefde.nl"]

    start_urls = ["http://boekenliefde.nl/editie-1243809-.html"]


    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        sites = hxs.select('//span/@itemprop').extract()
        for site in sites:
            print site.xpath('isbn')
            # print hxs.select('[@itemprop="isbn"]')
            # print hxs.select('[@itemprop="ratingValue"]')
            # print hxs.select('[@itemprop="bestRating"]')
            # print hxs.select('[@itemprop="ratingCount"]')
            # print hxs.select('[@itemprop="bookEdition"]')
            # print hxs.select('[@itemprop="numberOfPages"]')

