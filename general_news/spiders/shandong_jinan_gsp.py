# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request

from general_news.spiders.general import GeneralNewsSpider


class DahanColSpider(GeneralNewsSpider):
    name = 'shandong_jinan_gsp'
    project_name = scrapy.utils.project.get_project_settings().get('BOT_NAME')

    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         '{0}.basic_middleware.BasicMiddleware'.format(project_name): 500
    #     },
    #
    # }

    def start_requests(self):
        url_list=['http://fda.jinan.gov.cn/col/col10174/index.html?uid=10576&pageNum={}'.format(x) for x in range(1,306)]
        for url in url_list:
            yield Request(url,callback=self.parse)


    def parse(self, response):
        record=re.findall('<record>(.*?)</record>',response.body,re.S)
        for r in record:
            package = dict()

            package['href']='http://fda.jinan.gov.cn'+re.findall("<a href='(.*?)'",r,re.S)[0]
            package['date']=re.findall('#999">(.*?)</span>',r,re.S)[0][1:-1]
            if self.is_increment(package=package):
                yield Request(package['href'],callback=self.parse_article,meta=package)
