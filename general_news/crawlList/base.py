# encoding=utf8
import os


class newsBase(object):

    def __init__(self):

        self.data_dir = ''

        self.base_url = ''

        self.crawl_list = []

        self.contents_title_whitelist = []

        self.contents_title_xpath = ''

        self.contents_date_xpath = ''

        self.article_title_xpath = ''

        self.article_text_xpath = ''

        self.article_href_xpath = ''

    def clean_nrt(self, text):
        for each in ['\r', '\n', '\t', ' ']:
            text = text.replace(each, '')
        return text

    def strQ2B(self, ustring):
        """全角转半角"""
        rstring = ""
        for uchar in ustring:
            inside_code = ord(uchar)
            if inside_code == 12288:
                inside_code = 32
            elif 65281 <= inside_code <= 65374:
                inside_code -= 65248
            rstring += unichr(inside_code)
        return rstring

    def parse_title(self, title):
        return title

    def _parse_title(self,title):
        title_parsed = self.parse_title(title)
        return self.strQ2B(title_parsed.replace(' ', ''))

    def parse_date(self, date):
        return date

    def _parse_date(self, date):
        date_parsed = self.parse_date(date)
        return self.clean_nrt(date_parsed)

    def parse_text(self,text):
        return text

    def _parse_text(self, text):
        text_parsed=self.parse_text(text)
        return self.strQ2B(text_parsed)

    def parse_content_response(self, response):
        return response

    def parse_article_response(self, response):
        return response

    def parse_content_href(self, href):
        if self.base_url not in href:
            href = 'http://' + self.base_url + href
        if 'http://' not in href:
            href = 'http://' + self.base_url
        return href

    def parse_article_href(self, href):
        if self.base_url not in href:
            href = 'http://' + self.base_url + href
        if 'http://' not in href:
            href = 'http://' + href
        return href

    def parse_package(self, package):
        return package
