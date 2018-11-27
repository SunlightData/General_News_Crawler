# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.base_url = 'syjj.laiwu.gov.cn'

        self.contents_title_whitelist = ['GSP']

        self.article_title_xpath = '//*[@id="c"]/tr[1]/td'

        self.article_text_xpath = '//*[@id="c"]/tr[3]/td'

        self.article_href_xpath = ''

    def parse_article_href(self, href):
        print href
        return 'http://'+self.base_url+href[1:]
