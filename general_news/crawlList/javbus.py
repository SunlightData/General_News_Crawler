# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):
    '''
    国家市场监督管理总局
    首页》新闻》要闻》文件发布
    '''

    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'www.javbus.info'

        self.crawl_list = ['http://www.javbus.info/actresses/{}'.format(str(y)) for y in range(1, 778)]

        self.contents_title_xpath = '//*[@id="waterfall"]/div[*]/a'

        self.contents_date_xpath = './text()'

        self.article_title_xpath = '//*[@id="waterfall"]/div[1]/div/div[2]/span'

        self.article_text_xpath = '//*[@id="waterfall"]/div[1]/div/div[2]'

        self.article_href_xpath = ''

    def parse_date(self, date):
        return '2018-01-01'

    def parse_content_href(self, href):
        return 'http://' + href
