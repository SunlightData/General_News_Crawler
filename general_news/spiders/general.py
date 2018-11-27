# -*- coding: utf-8 -*-
import HTMLParser
import base64
import datetime
import random
import hashlib
import requests
import scrapy
import os
import sys
import logging

reload(sys)
sys.setdefaultencoding('utf-8')


class GeneralNewsSpider(scrapy.Spider):
    name = 'general'
    project_name = scrapy.utils.project.get_project_settings().get('BOT_NAME')
    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         '{0}.basic_middleware.BasicMiddleware'.format(project_name): 500
    #     },
    #
    # }

    def __init__(self, mode=0, increment_date=None, name=None, *args, **kwargs):
        '''
        :param mode: # 0-增量爬取 1-全量爬取 99-测试模式（测试模式只返回一条完整数据）
        :param increment_date: # 当指定为增量爬取时，指定一个日期，即从该日期开始增量爬取
        :param name: crawler名字
        '''
        self.name = name
        super(GeneralNewsSpider, self).__init__(*args, **kwargs)
        try:
            self.index = __import__('{0}.crawlList.{1}'.format(self.project_name, name), fromlist=(name,)).news()
        except ImportError:
            raise ImportError('{0}/crawlList/{1}.py is not exist !'.format(self.project_name, name))

        if not name:
            raise Exception('Spider not specified! Use -a name={SPIDER_NAME_FILE} instead.')

        self.isAll = True if int(mode) == 1 else False
        self.isTest = True if int(mode) == 99 else False
        self.isIncrement=True if int(mode)==2 else False

        if self.isAll:
            logging.warning('Run in FULL-CRAWL Mode!')
        else:
            logging.warning('Run in TEST/PART-CRAWL Mode!')
        self.base_url = self.index.base_url
        self.today = datetime.datetime.today().strftime('%Y-%m-%d')

        if increment_date and self.isIncrement:  # 从指定日期增量爬取
            self.today = increment_date

    def start_requests(self):
        crawl_list = self.index.crawl_list
        if self.isTest:
            test_url = crawl_list[0]
            logging.warning('\nContent URL: {0}\n'.format(test_url))
            yield scrapy.Request(test_url, callback=self.parse_content)
        else:
            for url in crawl_list:
                yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        # if self.isTest:
        #     print [response.body]
        response = self.index.parse_content_response(response)
        package = {}
        content_list = response.xpath(self.index.contents_title_xpath)  # 目录页Xpath
        article_per_page = len(content_list)
        if article_per_page == 0:
            raise Exception('contents_title_xpath is incorrect!')
        if article_per_page > 0:
            logging.warning('\nCount:{0} articles per content page\n'.format(article_per_page))

            if self.isTest:  # 测试模式只取第一个URL
                content_list = [content_list[0]]

            for title in content_list:
                try:
                    title_href = title.xpath('@href').extract_first().replace(r'..', '')
                except:
                    raise Exception('contents_title_xpath_href is incorrect! Try the location of xpath which source like \'<a href ..>\'  instead!')

                title_href = title_href.replace('http://', '').replace('https://', '')

                title_href_parsed = self.index.parse_content_href(title_href)

                if not title_href_parsed:
                    raise Exception('parse_content_href() is incorrect!')

                if self.isTest:
                    logging.warning('\nArticle URL:{0}\n'.format(title_href_parsed))
                try:
                    date = title.xpath(self.index.contents_date_xpath).extract_first()
                except:
                    raise Exception(
                        'CONTENTS_DATE_XPATH is incorrect! Please give the CONTENTS_DATE_XPATH node by using '
                        'CONTENT_TITLE_XPATH as the root node.')

                if self.is_increment(date=date):
                    package['date'] = date
                package['href'] = title_href_parsed
                yield scrapy.Request(title_href_parsed, callback=self.parse_article, meta=package)  # 对每个标题单独请求独立页面

    def is_increment(self, date=None, package={}):
        if not package.has_key('date'):
            date_parsed = self.index._parse_date(date)

            if not date_parsed:
                raise Exception('parse_date() is incorrect!')

            if self.isTest:
                logging.warning('\nArticle Date:{0},{1}\n'.format(date_parsed, str([date_parsed])))

        else:
            date_parsed = package['date']
        try:
            datetime.datetime.strptime(date_parsed, '%Y-%m-%d')
        except:
            raise Exception('Date format check failed! %Y-%m-%d date formatted instead!')

        if self.isAll == 0 and date_parsed <= self.today and not self.isTest:
            return False
        return date_parsed

    def parse_article(self, response):
        # if self.isTest:
        #      print [response.text]
        response = self.index.parse_article_response(response)
        package = response.meta
        try:
            article_title = response.xpath(self.index.article_title_xpath).xpath('string(.)').extract()[0]
        except:
            raise Exception('article_title_xpath is incorrect!')

        article_title_parsed = self.index._parse_title(article_title)

        if not article_title_parsed:
            raise Exception('parse_title() is incorrect!')
        package['title'] = article_title_parsed
        white_list_sign = 0
        if self.isTest:
            logging.warning('\nArticle Title:{0}\n'.format(article_title_parsed))

        else:
            for whitetitle in self.index.contents_title_whitelist:
                if whitetitle.lower() in package['title'].lower():
                    white_list_sign = 1
        if white_list_sign == 0 and self.index.contents_title_whitelist and not self.isTest:
            return

        try:
            article_text = response.xpath(self.index.article_text_xpath)
        except:
            raise Exception('article_text_xpath is incorrect!')

        package['source'] = article_text.extract_first()

        article_text_parsed = self.index._parse_text(article_text.xpath('string(.)').extract_first())
        if not article_text_parsed:
            raise Exception('parse_article_text() is incorrect!')

        if self.isTest:
            logging.warning('\nArticle Text:{0}...\n'.format(article_text_parsed[:200]))

        package['text'] = article_text_parsed

        package['attachment'] = []

        if self.index.article_href_xpath:
            try:
                articlehref = response.xpath(self.index.article_href_xpath).extract()  # 文章中的链接
                articlehref = list(set(articlehref))
            except:
                raise Exception('article_href_xpath is incorrect!')

            for each_href in articlehref:
                each_href = each_href.replace('http://', '').replace('https://', '')
                url = self.index.parse_article_href(each_href)
                if not url:
                    raise Exception('parse_article_href() is incorrect!')
                if self.isTest:
                    logging.warning('Article Attachment:{0}'.format(url))
                m2 = hashlib.md5()
                m2.update(url)
                md5_url = m2.hexdigest()
                package['attachment'].append({'url': url, 'filename': md5_url})

        package['project'] = self.name

        yield self.index.parse_package(package)
