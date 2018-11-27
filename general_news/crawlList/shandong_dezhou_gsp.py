# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'www.dzfda.gov.cn'

        self.crawl_list = ['http://www.dzfda.gov.cn/n2566547/n2566938/index_27262338_{}.html'.format(str(y)) for y in range(1, 31)]
        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '/html/body/ul/li[*]/a'

        self.contents_date_xpath = '../span/text()'

        self.article_title_xpath = '/html/body/div[5]/div[1]/div[2]/h1'

        self.article_text_xpath = '/html/body/div[5]/div[1]/div[2]/div[1]'

        self.article_href_xpath = ''

