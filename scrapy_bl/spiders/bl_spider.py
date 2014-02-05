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

        isbn = hxs.select('//span[@itemprop="isbn"]/text()').extract()
        ratingValue = hxs.select('//span[@itemprop="ratingValue"]/text()').extract()
        bestRating = hxs.select('//span[@itemprop="bestRating"]/text()').extract()
        ratingCount = hxs.select('//span[@itemprop="ratingCount"]/text()').extract()
        bookEdition = hxs.select('//span[@itemprop="bookEdition"]/text()').extract()
        numberOfPages = hxs.select('//span[@itemprop="numberOfPages"]/text()').extract()

        print isbn, numberOfPages, ratingValue, bookEdition
