# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):

    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'www.hzfda.gov.cn/'
        self.crawl_list = [
            'http://www.hzfda.gov.cn/Article_Search.asp?Field=Title&Keyword=GSP&ClassID=0&page={}'.format(str(y)) for y
            in range(1, 11)]

        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '/html/body/table[2]/tr/td/table/tr[1]/td/table/tr[2]/td/table/tr/td[3]/table/tr/td/table/tr[1]/td/table[*]/tr/td/a'

        self.contents_date_xpath = '../text()[2]'

        self.article_title_xpath = '/html/body/table[2]/tr/td/table/tr/td/table/tr/td[3]/table/tr/td/table/tr[1]/td/div'

        self.article_text_xpath = '/html/body/table[2]/tr/td/table/tr/td/table/tr/td[3]/table/tr/td/table/tr[5]/td'

        self.article_href_xpath = '/html/body/table[2]/tr/td/table/tr/td/table/tr/td[3]/table/tr/td/table/tr[5]/td//@href'

    def parse_date(self, date):
        tm=date.decode('utf8')[3:-1]
        tm=re.findall(u'(.*?)年(.*?)月(.*?)日',tm,re.S)[0]
        date='-'.join(tm)
        return self.clean_nrt(date)
