# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'sy.binzhou.gov.cn'

        self.crawl_list = ['http://sy.binzhou.gov.cn/zhengwu/class/?0.html&page={}&showtj=&showhot=&author=&key=&code='.format(str(y)) for y in range(1, 10)]
        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '//*[@id="container"]/div[1]/div[3]/ul/ul/li[*]/a'

        self.contents_date_xpath = '../div/text()'

        self.article_title_xpath = '//*[@id="topic"]/h1'

        self.article_text_xpath = '//*[@id="nw_content"]'

        self.article_href_xpath = '//*[@id="nw_content"]//@href'

    def parse_content_href(self, href):
        return 'http://'+self.base_url+href[1:].replace('/zhengwu/html/','/zhengwu/html/?')
