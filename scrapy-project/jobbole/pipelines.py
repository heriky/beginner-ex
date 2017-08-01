# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JobbolePipeline(object):
    def process_item(self, item, spider):
        return item


class DeriveImagesPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for status, value in results:
            item['face_url_path'] = value["path"]
        return super(DeriveImagesPipeline, self).item_completed(results, item, info) #  python中调用父类方法的方式
