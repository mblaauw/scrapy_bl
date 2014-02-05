# Scrapy settings for scrapy_bl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrapy_bl'

SPIDER_MODULES = ['scrapy_bl.spiders']
NEWSPIDER_MODULE = 'scrapy_bl.spiders'


CONCURRENT_REQUESTS = 6

CONCURRENT_REQUESTS_PER_DOMAIN = 6

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_bl (+http://www.yourdomain.com)'
