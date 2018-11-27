# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request

from general_news.spiders.general import GeneralNewsSpider


class DahanColSpider(GeneralNewsSpider):
    name = 'shandong_zibo_gsp'
    project_name = scrapy.utils.project.get_project_settings().get('BOT_NAME')

    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         '{0}.basic_middleware.BasicMiddleware'.format(project_name): 500
    #     },
    #
    # }

    def start_requests(self):
        url_list=['http://fda.zibo.gov.cn/col/col2139/index.html?uid=10539&pageNum={}'.format(x) for x in range(1,51)]
        for url in url_list:
            yield Request(url,callback=self.parse)


    def parse(self, response):
        record=re.findall('<record>(.*?)</record>',response.body,re.S)
        for r in record:
            package = dict()
            package['href']='http://fda.zibo.gov.cn'+re.findall("<a href='(.*?)'",r,re.S)[0]
            package['date']=re.findall('<span>(.*?)</span>',r,re.S)[0][1:-1]
            if self.is_increment(package=package):
                yield Request(package['href'],callback=self.parse_article,meta=package)
