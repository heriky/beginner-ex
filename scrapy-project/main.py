# -*- coding: utf8 -*-
from scrapy.cmdline import execute
import sys
import os

__author__ = 'hankang'

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
spider_path = os.path.join(os.path.dirname(__file__), './jobbole/spiders/jobbole_spider.py')
spider_path = os.path.abspath(spider_path)

execute(['scrapy', 'runspider', spider_path])

