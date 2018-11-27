# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.base_url = 'fda.zibo.gov.cn'

        self.contents_title_whitelist = ['GSP']

        self.article_title_xpath = '//*[@id="barrierfree_container"]/div[1]/div[3]/div[2]/div[1]/div[1]'

        self.article_text_xpath = '//*[@id="barrierfree_container"]'

        self.article_href_xpath = ''

    def parse_article_href(self, href):
        return 'http://'+self.base_url+href[1:]
