# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'lyfda.linyi.gov.cn'

        self.crawl_list = ['http://lyfda.linyi.gov.cn/gsgg/gsgg/{}.htm'.format(str(y)) for y in range(1, 34)]
        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '/html/body/div/div[5]/div[2]/div[2]/ul/li[*]/a'

        self.contents_date_xpath = '../span/text()'

        self.article_title_xpath = '/html/body/div/div[5]/div[2]/div[2]/form/h1'

        self.article_text_xpath = '/html/body/div/div[5]/div[2]/div[2]/form/div/div'

        self.article_href_xpath = ''

