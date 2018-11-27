# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):


    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'www.dyfda.gov.cn'

        self.crawl_list = ['http://www.dyfda.gov.cn/CL0032/index_{}.html'.format(str(y)) for y in range(1, 34)] + [
            'http://www.dyfda.gov.cn/CL0032/index.html']

        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '//*[@id="box"]/div[1]/div[3]/div[2]/table[1]/tbody/tr[*]/td[1]/a'

        self.contents_date_xpath = '../span/text()'

        self.article_title_xpath = '//*[@id="box"]/div/div[1]/div/table/tbody/tr[1]/td'

        self.article_text_xpath = '//*[@id="box"]/div/div[1]/div/table/tbody'

        self.article_href_xpath = ''

    def parse_date(self, date):
        return self.clean_nrt(date)[1:-1]
