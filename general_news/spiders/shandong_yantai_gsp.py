# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request

from general_news.spiders.general import GeneralNewsSpider


class DahanColSpider(GeneralNewsSpider):
    name = 'shandong_yantai_gsp'
    project_name = scrapy.utils.project.get_project_settings().get('BOT_NAME')

    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         '{0}.basic_middleware.BasicMiddleware'.format(project_name): 500
    #     },
    #
    # }

    def start_requests(self):
        url_list = ['http://fda.yantai.gov.cn/col/col3163/index.html?uid=26208&pageNum={}'.format(x) for x in range(1, 83)]
        for url in url_list:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        print response.url
        record = re.findall('<record>(.*?)</record>', response.body, re.S)
        for r in record:
            package = dict()
            package['href'] = 'http://fda.yantai.gov.cn' + re.findall('<a href="(.*?)"', r, re.S)[0]

            package['date'] = re.findall(r'>\[(.*?)\]</td>', r, re.S)[0]
            if self.is_increment(package=package):
                yield Request(package['href'], callback=self.parse_article, meta=package)
