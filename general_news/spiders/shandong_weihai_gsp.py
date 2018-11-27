# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request

from general_news.spiders.general import GeneralNewsSpider


class DahanColSpider(GeneralNewsSpider):
    name = 'shandong_weihai_gsp'
    project_name = scrapy.utils.project.get_project_settings().get('BOT_NAME')

    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         '{0}.basic_middleware.BasicMiddleware'.format(project_name): 500
    #     },
    #
    # }

    def start_requests(self):
        url_list = ['http://www.weihaifda.gov.cn/col/col14251/index.html']
        for url in url_list:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        print response.url
        record = re.findall("urls\[i\]='(.*?)';headers\[i\]='(.*?)';year\[i\]='(.*?)';month\[i\]='(.*?)';day\[i\]='(.*?)';", response.body, re.S)
        for r in record:
            package = dict()
            package['href'] = 'http://www.weihaifda.gov.cn' + r[0]

            package['date'] = r[2]+'-'+r[3]+'-'+r[4]
            if self.is_increment(package=package):
                yield Request(package['href'], callback=self.parse_article, meta=package)
