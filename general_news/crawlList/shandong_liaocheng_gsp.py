# encoding=utf8
import re

import chardet

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):
    
    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'www.liaocheng.gov.cn/xxgk/szfbmxxgk/sspypjdglj/'

        self.crawl_list = ['http://www.liaocheng.gov.cn/xxgk/szfbmxxgk/sspypjdglj/216/list_593_{}.html'.format(str(y)) for y in range(1, 21)]+['http://www.liaocheng.gov.cn/xxgk/szfbmxxgk/sspypjdglj/216/list_593.html']
        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '//*[@id="documentContainer"]/div[*]/li[2]/div/a'

        self.contents_date_xpath = './@href'

        self.article_title_xpath = '//*[@id="gkml"]/div/div/div[2]/h2'

        self.article_text_xpath = '//*[@id="Zoom"]'

        self.article_href_xpath = ''

    def parse_date(self, date):
        date=re.findall('t(.*?)_',date,re.S)[0]
        date=date[0:4]+'-'+date[4:6]+'-'+date[6:8]
        return self.clean_nrt(date)