# -*- coding: utf-8 -*-
import HTMLParser
import re

import scrapy
from scrapy import Request

from general_news.spiders.general import GeneralNewsSpider

def decodeHtml(input):
    h = HTMLParser.HTMLParser()
    s = h.unescape(input)
    return s

class DahanColSpider(GeneralNewsSpider):
    name = 'shandong_laiwu_gsp'
    project_name = scrapy.utils.project.get_project_settings().get('BOT_NAME')

    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         '{0}.basic_middleware.BasicMiddleware'.format(project_name): 500
    #     },
    #
    # }

    def start_requests(self):
        url_list = ['http://syjj.laiwu.gov.cn/col/col3242/index.html']
        for url in url_list:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        body=decodeHtml(response.body)
        record = re.findall('<record>(.*?)</record>', body, re.S)
        for r in record:
            package = dict()
            package['href'] = 'http://syjj.laiwu.gov.cn' + re.findall('href=\'(.*?)\'', r, re.S)[0]
            date=re.findall(r"href='/art/(.*?)/(.*?)/(.*?)/", r, re.S)[0]
            package['date'] =date[0]+'-'+date[1].zfill(2)+'-'+date[2]
            if self.is_increment(package=package):
                yield Request(package['href'], callback=self.parse_article, meta=package)
