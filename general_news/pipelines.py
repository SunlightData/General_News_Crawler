# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

import os
import scrapy
from scrapy.pipelines.files import FilesPipeline


class GeneralPipeline(object):

    def process_item(self, item, spider):
        parsed_data = dict()
        parsed_data['attachment'] = item['files']
        del item['files']
        parsed_data.update(item)

        result = {
            'meta_version': '',
            'meta_updated': datetime.datetime.now().isoformat()[:19],
            'download_config': {
                'url': item["href"],
                'method': 'GET'
            },
            'download_data': {
                'parsed_data': parsed_data,
                'raw_data': {},
            }
        }

        return result


class GeneralFilePipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        for attachment in item.get('attachment', []):
            yield scrapy.Request(
                url=attachment['url'],
                meta={'source': item['project'], 'name': attachment['filename']},
            )

    def file_path(self, request, response=None, info=None):
        time_now = datetime.datetime.now().strftime('%Y%m%d')
        pre = "{}_{}".format(request.meta['source'], time_now)
        media_guid = request.meta['name']
        media_ext = os.path.splitext(request.url)[1]
        return '%s/%s%s' % (pre, media_guid, media_ext)
