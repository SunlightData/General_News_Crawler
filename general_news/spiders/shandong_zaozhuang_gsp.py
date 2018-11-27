# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import FormRequest

from general_news.spiders.general import GeneralNewsSpider


class NewsSpider(GeneralNewsSpider):
    name = 'shandong_zaozhuang_gsp'
    project_name = scrapy.utils.project.get_project_settings().get('BOT_NAME')

    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         '{0}.basic_middleware.BasicMiddleware'.format(project_name): 500
    #     },
    # 
    # }

    def start_requests(self):
        url='http://www.zzfda.gov.cn/webnoticelist.shtml'
        for x in range(89):
            yield FormRequest(url,formdata={'fuzzy_title':'', 'gtype': '2','pageNum': x},callback=self.parse_content)


