# -*- coding: utf-8 -*- 
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.selector import HtmlXPathSelector


class ScrapySpider(CrawlSpider):
    name = "lower"
    allowed_domains = ["yaca.yandex.ru"]
    start_urls = ["http://yaca.yandex.ru/yca/cat/"]
    rules = (
        Rule(SgmlLinkExtractor(allow=('yaca.yandex.ru/yca/cat/[a-zA-Z]'),
                               deny=('\d+|lnd.novo-play.ru|pda.kvner.ru')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[2]/dl/dt[1]')
        items = []
        if sites == []:
            open("lower_branches.t", "ab").write(response.url + "\n")
