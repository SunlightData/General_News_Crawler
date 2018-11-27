# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'www.wffda.gov.cn/FLZZ/YP/TZGG'

        self.crawl_list = ['http://www.wffda.gov.cn/FLZZ/YP/TZGG/index_{}.html'.format(str(y)) for y in range(1, 50)] + [
            'http://www.wffda.gov.cn/FLZZ/YP/TZGG/index.html']

        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '/html/body/div[3]/table/tr/td[3]/div[2]/table/tr[1]/td/table/tr[*]/td[2]/a'

        self.contents_date_xpath = '../../td[3]/text()'

        self.article_title_xpath = '/html/body/div[3]/table/tr/td/div[2]/h4'

        self.article_text_xpath = '/html/body/div[3]/table/tr/td/div[2]'

        self.article_href_xpath = ''

    def parse_content_href(self, href):
        return 'http://'+self.base_url+href[1:]
