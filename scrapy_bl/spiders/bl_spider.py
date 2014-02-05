__author__ = 'MICH'
import re
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy_bl.items import ScrapyBlItem


class BlSpider(BaseSpider):
    name = "bl"
    allowed_domains = ["boekenliefde.nl"]
    start_urls = []
    #2543810
    for i in range(9999, 2543810):
        new_url = "http://boekenliefde.nl/editie-" + str(i) + "-.html"
        start_urls.append(new_url)


    def parse(self, response):
        items = []

        hxs = HtmlXPathSelector(response)

        item = ScrapyBlItem()
        item['isbn'] = hxs.select('//span[@itemprop="isbn"]/text()').extract()
        item['ratingValue'] = hxs.select('//span[@itemprop="ratingValue"]/text()').extract()
        item['bestRating'] = hxs.select('//span[@itemprop="bestRating"]/text()').extract()
        item['ratingCount'] = hxs.select('//span[@itemprop="ratingCount"]/text()').extract()
        item['bookEdition'] = hxs.select('//span[@itemprop="bookEdition"]/text()').extract()
        item['numberOfPages'] = hxs.select('//span[@itemprop="numberOfPages"]/text()').extract()

        #item['Translator'] = hxs.select('//*[@id="bookinfo"]/div[4]/div[2]/a/text()').extract()
        #item['Details'] = hxs.select('//*[@id="bookinfo"]/div[3]/div[2]/text()').extract()
        #item['EditionDetails'] = hxs.select('//*[@id="bookinfo"]/div[2]/div[2]/text()').extract()
        #item['Illustrations'] = hxs.select('//*[@id="bookinfo"]/div[3]/div[2]/a/text()').extract()

        items.append(item)

        return items

