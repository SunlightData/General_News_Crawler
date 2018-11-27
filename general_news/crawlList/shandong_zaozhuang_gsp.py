# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'www.zzfda.gov.cn/'

        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[*]/a'

        self.contents_date_xpath = '../span/text()'

        self.article_title_xpath = '/html/body/div[4]/div/div[2]/span'

        self.article_text_xpath = '/html/body/div[4]/div/div[3]'

        self.article_href_xpath = '/html/body/div[4]/div/div[3]//@href'

    def parse_date(self, date):
        return date[1:-1]
