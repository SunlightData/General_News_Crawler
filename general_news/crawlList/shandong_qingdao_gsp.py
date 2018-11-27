# encoding=utf8
import re

import chardet
from w3lib.encoding import html_to_unicode

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):
    
    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = ''

        self.base_url = 'sfda.qingdao.gov.cn'

        self.crawl_list = ['http://sfda.qingdao.gov.cn/n32205902/n32205907/n32205908/index.html']

        self.contents_title_whitelist = ['GSP']

        self.contents_title_xpath = '//*[@id="listChangeDiv"]/ul/li[*]/a'

        self.contents_date_xpath = '../span/text()'

        self.article_title_xpath = '/html/body/div[2]/div[2]/div[1]/h1'

        self.article_text_xpath = '/html/body/div[2]/div[2]/div[2]'

        self.article_href_xpath = ''

    def parse_article_response(self, response):
        response._cached_ubody = response.body.decode('utf8')
        return response

    def parse_date(self, date):
        return self.clean_nrt(date)

    def parse_package(self, package, isTest=False):
        package['newsCategory'] = '首页》新闻》要闻》文件发布'
        attachment = []
        for each in package['attachment']:
            date = re.findall('http://samr.saic.gov.cn/xw/yw/wjfb/(.*?)/t', package['href'], re.S)[0]
            each['url'] = 'http://samr.saic.gov.cn/xw/yw/wjfb/' + date + '/' + each['url'][8:]
            attachment.append(each)
        return package
