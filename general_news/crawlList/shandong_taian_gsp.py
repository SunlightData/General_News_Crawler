# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'www.tafda.gov.cn'

        self.crawl_list = ['http://www.tafda.gov.cn/a/xinxigongkai/shuanggongshi/xingzhengxukegongshi/list_47_{}.html'.format(str(y)) for y in range(1, 12)]
        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '/html/body/div[2]/div[1]/div[2]/ul/li[*]/a'

        self.contents_date_xpath = '../span/text()'

        self.article_title_xpath = '/html/body/div[2]/div[1]/div[2]/div[1]/h2'

        self.article_text_xpath = '/html/body/div[2]/div[1]/div[2]/div[3]'

        self.article_href_xpath = '/html/body/div[2]/div[1]/div[2]/div[3]//@href'

