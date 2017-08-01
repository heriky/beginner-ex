# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobboleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    post_time = scrapy.Field()
    tags = scrapy.Field()
    source_url = scrapy.Field()
    upvote_count = scrapy.Field()
    comment_count = scrapy.Field()
    face_url = scrapy.Field()
    face_url_path = scrapy.Field() # 下载好的图片，本地保存地址
    id = scrapy.Field()
