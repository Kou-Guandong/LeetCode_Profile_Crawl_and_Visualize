import scrapy
import re
from datetime import date
from scrapy.loader import ItemLoader
from ..items import Profile


class ProfileSpider(scrapy.Spider):
    name = "profiles"

    def __init__(self):
        with open('./profile_urls.txt') as f:
            self.start_urls = f.readlines()

    def parse(self, response):
        solved_over_all = response.xpath(
            '//h3[text()="Progress"]/ancestor::div[@class="panel panel-default"]//li[1]/span[@class="badge progress-bar-success"]/text()'
        ).extract()[0].strip()
        solved = re.findall('(\d+)\\.*', solved_over_all)[0]
        username = response.xpath(
            '//p[@class="username"]/text()').extract()[0].strip()

        l = ItemLoader(item=Profile(), response=response)
        l.add_value('name', username)
        l.add_value('solved', solved)
        l.add_value('date', date.today().strftime("%Y-%m-%d"))
        return l.load_item()
