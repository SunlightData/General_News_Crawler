# encoding=utf8
import re

from general_news.crawlList.base import newsBase


# DONE

class news(newsBase):
    '''
    国家市场监督管理总局
    首页》新闻》要闻》文件发布
    '''

    def __init__(self):
        newsBase.__init__(self)

        self.data_dir = 'samr'

        self.base_url = 'samr.saic.gov.cn'

        self.crawl_list = ['http://samr.saic.gov.cn/xw/yw/wjfb/index_{}.html'.format(str(y)) for y in range(1, 3)] + [
            'http://samr.saic.gov.cn/xw/yw/wjfb/index.html']

        self.contents_title_whitelist = []

        self.contents_title_xpath = '/html/body/div[7]/div[1]/ul[*]/li[1]/a'

        self.contents_date_xpath = '../../li[2]/text()'

        self.article_title_xpath = '/html/body/div[4]/div[2]/div[2]/ul[1]/li[1]'

        self.article_text_xpath = '/html/body/div[4]/div[2]/div[2]/div[1]/div'

        self.article_href_xpath = '/html/body/div[4]/div[2]/div[2]/ul[2]//@href'

    def parse_content_href(self, href):
        if self.base_url not in href:
            href = 'http://samr.saic.gov.cn/xw/yw/wjfb/' + href[1:]
        return href

    def parse_article_href(self, href):
        if self.base_url not in href:
            href = href[1:]
        if 'http://' not in href:
            href = 'http://' + href
        return href

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
