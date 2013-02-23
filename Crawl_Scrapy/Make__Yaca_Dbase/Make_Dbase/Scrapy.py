# -*- coding: utf-8 -*- 
import re
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from tutorial.items import Scr1Item
from scrapy.contrib.loader.processor import Compose
from scrapy.contrib.loader.processor import MapCompose
from scrapy.contrib.loader.processor import TakeFirst

class Scr1Spider(CrawlSpider):
    name = "make"
    allowed_domains = ["yaca.yandex.ru"]
    #insert_here_lower_branches_url
    start_urls = ["http://yaca.yandex.ru/yca/cat/Entertainment/Games/game-play/MMOG/RPG/",
"http://yaca.yandex.ru/yca/cat/Entertainment/Games/game-play/MMOG/RPG/",
"http://yaca.yandex.ru/yca/cat/Entertainment/Games/game-play/MMOG/Sport_Management/",
"http://yaca.yandex.ru/yca/cat/Entertainment/Games/game-play/New_Year/",
"http://yaca.yandex.ru/yca/cat/Entertainment/Games/game-play/New_Year/Flashgames/",
"http://yaca.yandex.ru/yca/cat/Entertainment/Games/game-play/New_Year/Minigames/",
"http://yaca.yandex.ru/yca/cat/Entertainment/Games/game-play/New_Year/Social_games/",
]
    rules = (
        Rule(SgmlLinkExtractor(allow=('\d+.html')),  callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=('0.html')),  callback='parse_item', follow=True),
     ) 
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ol/li')
        items = []
        for site in sites:
            item = Scr1Item()
            item['link'] = site.select('h3/a[1]/@href').extract()
            item['file1'] = response.url
            items.append(item)
        return items
   
