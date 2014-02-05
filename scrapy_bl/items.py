# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrapyBlItem(Item):
    # define the fields for your item here like:
    # name = Field()
    isbn = Field()
    ratingValue = Field()
    bestRating = Field()
    ratingCount = Field()
    bookEdition = Field()
    numberOfPages = Field()
    #Translator = Field()
    #Details = Field()
    #EditionDetails = Field()
    #Illustrations = Field()
    pass
